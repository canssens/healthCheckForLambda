import urllib2
from urllib2 import urlopen
import os
import boto3
import json


SMS_DEST = os.environ['sms_dest'] # 336XXXXXXXX
SITES = os.environ['sites']  # URL of the sites , separated by ";"
ARN = os.environ['arn'] #arn of the topic

def alertMe(app):
	print "Alert for %s" % app
	

	messageText = 'DOWN %s' %  app
	message = {"Message":  messageText}
	client = boto3.client('sns')
	response = client.publish(
	    TargetArn=ARN,
	    Message=json.dumps({'default': json.dumps(message)}),
	    MessageStructure='json'
	)




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
