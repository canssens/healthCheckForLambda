# healtCheckForLambda
HealthCheck in Python with notification with the Next API

You have to set up some env var :
NEXMO_API_KEY
NEXMO_API_SECRET
SMS_DEST
SMS_SENDER
SITES

My AWS Lambda Conf :
AWSTemplateFormatVersion: '2010-09-09'
Transform: 'AWS::Serverless-2016-10-31'
Description: status
Resources:
  HealthCheck:
    Type: 'AWS::Serverless::Function'
    Properties:
      Handler: lambda_function.lambda_handler
      Runtime: python2.7
      CodeUri: .
      Description: status
      MemorySize: 128
      Timeout: 30
      Role: 'xxxxx/HealthCheckRole'
      Events:
        Schedule1:
          Type: Schedule
          Properties:
            Schedule: rate(5 minutes)
      Environment:
        Variables:
          sms_sender: 'xxxxx'
          nexmo_api_key: xxxxx
          sites: >-
            http://www.perdu.com/;http://www.perdu.com
          sms_dest: '33659xxxxx'
          nexmo_api_secret: xxxx
