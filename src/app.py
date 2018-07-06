#!/usr/bin/python
from http.server import BaseHTTPRequestHandler,HTTPServer
from urllib.parse import urlparse
import RESTSplunkMethods as splunk
import wrapper
import helper
import os

PORT_NUMBER = 8080
baseurl = 'https://localhost:8089'
username = os.environ.get('SPLUNK_USERNAME_LOCAL')
password = os.environ.get('SPLUNK_PASSWORD_LOCAL')

splunk.connect(baseurl, username, password)

def toCamelCase(str):
	str = str.lower()
	components = str.split(' ')
	# Capitalize the first letter of each component except the first one
	# with the 'title' method and join them together.
	return components[0] + ''.join(x.title() for x in components[1:])

# This class will handle any incoming request from the browser 
class myHandler(BaseHTTPRequestHandler):
	
	# Handler for POST requests
	def do_POST(self):
		contentLength = int(self.headers['Content-Length']) # <--- Gets the size of data
		postBody = (self.rfile.read(contentLength)).decode('utf-8') # <--- Gets the data itself
		
		# Extract the command and the parameters from the postBody
		command = postBody.split(', ')[0]
		originalCommand = command
		parameters = postBody.split(', ', 3)[1:]
		function = None
		
		command = toCamelCase(command)
		
		if command == "splunkbot":
			function = helper.listCommands
		elif len(parameters) > 0 and parameters[0] == "help":
			function = getattr(helper, "%s" % "getCommandHelp")
			parameters = command
		else:
			# Define the wrapper function to call
			function = getattr(wrapper, "%s" % command)
		
		# Configure the response. Always return 201 even if an exception downstream is returned
		self.send_response(201)
		self.send_header('Content-type','text/html')
		self.end_headers()
		
		try:
			results = "%s" % function(parameters)
			self.wfile.write(bytes(results, 'utf8'))
		except Exception as e:
			print(e)
			e = "%s: %s \n\n\nSplunkBot Help:\nSend 'splunkbot' to list available commands.\nSend '%s, help' for help with this command" % (type(e).__name__, e, originalCommand)
			self.wfile.write(bytes(e, 'utf8'))
		return

try:
	# Create a web server and define the handler to manage the incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print('[APP] Started httpserver on port ' , PORT_NUMBER)
	
	# Wait forever for incoming http requests
	server.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the web server')
	server.socket.close()