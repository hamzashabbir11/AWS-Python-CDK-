import json,boto3,os
from operator import itemgetter

"""
p=[{"event1":{"attr1": 10 }}]
print(p[0]["event1"]["attr1"])"""

def eventLambda(event,context):
    if event["httpMethod"]=="POST":
        data=event["body"]
        msg="DONE POST"
        s=json.loads(data)
        val=s[0]["event1"]["attr1"]
        datatime=event["requestContext"]["requestTime"][7:20]
        dataa=TabelPut(val,datatime)
        return {
            "statusCode": 200,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.dumps(msg),
            "isBase64Encoded": False
        }

    
    if event["httpMethod"]=="GET":
        
        data=event["body"]
        a=getTableData()
        return {
            "statusCode": 200,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.dumps(a),
            "isBase64Encoded": False
        }
    



def TabelPut(val,time):
    tname=os.environ['TABLE_NAME']
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table(tname)
   
    table.put_item(
    Item={
        'value': val,
        'Time':time
        })
    
def getTableData():
    
    dynamodbTable = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodbTable.Table('AppDay2Stack-app2table9A638853-1C9VT5Y1WP1M0')
   
    response=table.scan()
   
    URLs_to_Monitor = response['Items']
    URL_Sorted_Time=sorted(URLs_to_Monitor,key=itemgetter('Time'))
    #Latest_Item=URL_Sorted_Time[:]
    return str(URL_Sorted_Time)
    

    
    