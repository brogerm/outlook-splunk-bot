"""
	A loose wrapper to extract the parameters from the POST request and send them to the Splunk methods
"""

import RESTSplunkMethods as splunk

def listSavedSearches(params):
	if len(params) > 0:
		return splunk.listSavedSearches(params[0])
	else:
		return splunk.listSavedSearches()
		
def listReportNames(params):
	if len(params) > 0:
		return splunk.listReportNames(params[0])
	else:
		return splunk.listReportNames()
		
def runSavedSearch(params):
	return splunk.runSavedSearch(params[0])
	
def runSearch(params):
	return splunk.runSearch(params[0])


def listDashboardNames(params):
	if len(params) == 2:
		return splunk.listDashboardNames(params[0],params[1])
	else:
		return splunk.listDashboardNames(params[0])

def listDashboardInputs(params):
	return splunk.listDashboardInputs(params[0],params[1])		
		

def getDashboardPdf(params):
	if len(params) == 3:
		return splunk.getDashboardPdf(params[0],params[1], params[2])
	else:
		return splunk.getDashboardPdf(params[0],params[1])
		
def getReportPdf(params):
	return splunk.getReportPdf(params[0])
	
def getSearchPdf(params):
	return splunk.getSearchPdf(params[0])

	
def listAlertNames(params):
	if len(params) > 0:
		return splunk.listAlertNames(params[0])
	else:
		return splunk.listAlertNames()

def disableAlert(params):
	if len(params) == 2:
		return splunk.disableAlert(params[0],params[1])
	else:
		return splunk.disableAlert(params[0])
		
def enableAlert(params):
	return splunk.enableAlert(params[0])
	
def listDisabledAlerts(params):
	if len(params) > 0:
		return splunk.listDisabledAlerts(params[0])
	else:
		return splunk.listDisabledAlerts()
		
def rescheduleAlert(params):
	return splunk.rescheduleAlert(params[0],params[1])
	
	
def listAppNames(params):
	if len(params) > 0:
		return splunk.listAppNames(params[0])
	else:
		return splunk.listAppNames()
		
