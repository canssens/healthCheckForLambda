import urllib
import urllib2
from urllib2 import urlopen
import os
from base64 import b64encode


NEXMO_API_KEY = os.environ['nexmo_api_key']
NEXMO_API_SECRET = os.environ['nexmo_api_secret']
SMS_DEST = os.environ['sms_dest'] # 336XXXXXXXX
SMS_SENDER = os.environ['sms_sender'] #alpha or number
SITES = os.environ['sites']  # URL of the sites , separated by ";"


def alertMe(app):
	print "Alert for %s" % app
	params = {
    'api_key': NEXMO_API_KEY,
    'api_secret': NEXMO_API_SECRET,
    'to': SMS_DEST,
    'from': SMS_SENDER,
    'text': 'DOWN %s' %  app
	}

	url = 'https://rest.nexmo.com/sms/json?' + urllib.urlencode(params)

	request = urllib2.Request(url)
	request.add_header('Accept', 'application/json')
	response = urllib2.urlopen(request)



def lambda_handler(event, context):
	sitesList = SITES.split(';')
	for site in sitesList:
		domainName = site.split("//")[-1].split("/")[0]
		try:
			if urlopen(site).getcode() != 200 :
				alertMe(domainName)
		except:
			print('Check failed!')
			alertMe(domainName)
		else:
			print('Check passed %s!'%domainName)
