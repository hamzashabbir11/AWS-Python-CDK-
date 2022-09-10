import json
import urllib3,boto3,os

def api_handler(event,context):
    
    #json.loads(event['body'])
    if event["httpMethod"] =="POST":
        url=event["body"]
        datatime=event["requestContext"]["requestTime"][7:20]
        y=TabelPut(url,datatime)
        return_data=url+datatime

        return {
        "statusCode": 201,
        "headers": {
            "content-type": "application/json"
        },
        "body": json.dumps(event),
        "isBase64Encoded": False
            }

    elif event["httpMethod"]=="GET":
        return {
            "statusCode": 200,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.dumps(event),
            "isBase64Encoded": False
        }

    elif event["httpMethod"]=="DELETE":
        body=json.loads(event["body"])

        URL_to_delete=body["url_name"]
        TIME=body["Time"]
        dell=DeleteURL(URL_to_delete,TIME)
       
        Output_String=URL_to_delete+TIME+" Deleted"

        return {
            "statusCode": 204,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.dumps(event),
            "isBase64Encoded": False
        }
    


                
                 
    #Execution failed due to configuration error: Malformed Lambda proxy response Wed Jul 13 06:46:47 UTC 2022 : Method completed with status: 502
    #Solution in next comment
    #https://aws.amazon.com/premiumsupport/knowledge-center/malformed-502-api-gateway/
    #print(event)

def TabelPut(url,time):
    tname=os.environ['TABLE_NAME']
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table(tname)
   
    table.put_item(
    Item={
        'url_name': url,
        'Time':time
        })
    

def DeleteURL(body,timee):
    tname=os.environ['TABLE_NAME']
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table(tname)

    response = table.delete_item(Key={
    'url_name': body,
    'Time' : timee
    })

























