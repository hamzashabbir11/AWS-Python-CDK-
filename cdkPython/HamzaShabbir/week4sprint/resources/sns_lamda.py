import boto3
import json,os
'''accesskeyid=os.environ.get('ACCESS_KEY_ID')
secretaccesskey=os.environ.get('AWS_SECRET_ACCESS_KEY')
aws_access_key_id=accesskeyid,
aws_secret_access_key=secretaccesskey,'''



def AlarmLamda(event,context):
    tname=os.environ['TABLE_NAME']
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table(tname)
    #parsing the event params
    y=event
    attribute1=y["Records"][0]["EventSource"]
    attribute2=y["Records"][0]["Sns"]["Message"]
    attribute3=y["Records"][0]["Sns"]["Timestamp"]
    attribute4=y["Records"][0]["Sns"]["MessageId"]
    print(attribute1,attribute2,attribute3)
    
    #creating boto3 clinet to put msg in dynamo db
   
    table.put_item(
    
    Item={
        'msgid': attribute4,
        'time':attribute3,
        'msg': attribute2,
        'source': attribute1
        })
           
    
    
    
    



    