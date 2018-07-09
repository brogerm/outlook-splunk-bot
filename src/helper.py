import RESTSplunkMethods as splunk
import wrapper
import inspect
import pydoc
import re


def formatCommand(str):
	lowerWord = re.findall('[a-z]*',str)
	upperWords = re.findall('[A-Z][^A-Z]*', str)
	
	formattedCommand = lowerWord[0]

	for word in upperWords:
		formattedCommand = formattedCommand + " " + word.lower()
		
	return formattedCommand
	

def listCommands(help):
	print("[HELPER] Listing all commands")
	allCommands = inspect.getmembers(wrapper, inspect.isfunction)

	commandList = []

	for command in allCommands:
		commandList.append(formatCommand(command[0]))
	
	commandList = "%s" % commandList
	return commandList.replace(',',',\n')
	
	
def getCommandHelp(command):
	print("[HELPER] Providing help for command: %s" % command)
	documentation = pydoc.render_doc(getattr(splunk, "%s" % command))
	return documentation.split(')',1)[1]	


def generateDocs():
	documentation = pydoc.render_doc(splunk, renderer=pydoc.plaintext)
	documentation = documentation.split('FUNCTIONS')
	documentation = documentation[1].split('sleep(...)')[0]
	file = open('docs.txt','w')
	file.write(documentation)
	file.close()
	
generateDocs()

