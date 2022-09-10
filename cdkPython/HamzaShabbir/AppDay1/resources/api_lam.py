import json
def apifunc(event,context):

    d={"arg1":11}
    
    if event["httpMethod"]=="GET":
        return {
            "statusCode": 200,
            "headers": {
                "content-type": "application/json"
            },
            "body": json.dumps(d),
            "isBase64Encoded": False
        }