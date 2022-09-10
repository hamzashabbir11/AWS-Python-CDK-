import urllib3
import json
import boto3,putMetric
NAMESPACE="Hamza App 1"

def monitorlam(event,context):

    url="https://naap4u78c2.execute-api.us-east-1.amazonaws.com/prod/monitor"
    http = urllib3.PoolManager()
    r = http.request('GET', url)
    a=json.loads(r.data)
    data=a["arg1"]

    print("Hello App 1", data)
    Latency1=putMetric.putMetriCloudWatch()
    Metric=Latency1.putData(NAMESPACE,Metricname='Data',Dimention=[{'Name': 'Data point','Value': url}],Value=data)
   

    

