import datetime
from itertools import count
from operator import itemgetter
import re
from urllib import response
import urllib3
import boto3,os
import putmetricClass
#URL1="http://www.skipq.org"
NAMESPCAE='HAMZASHABBIRWEBHEALTH'
import globalvars as gbvars
# boto3 documentaation 
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_data
def LambdaHandler(event,context):
    global URLfromTable
    URLfromTable=getTableData()
    x=healthchk(URLfromTable)
    y=latency(URLfromTable)
    print(URLfromTable)
    print("Hello This is week6 How are you holdin up ? ",x,y)
    Latency1=putmetricClass.putMetriCloudWatch()
    Health1=putmetricClass.putMetriCloudWatch()
    Metric1=Latency1.putData(NAMESPCAE,Metricname='Latency',Dimention=[{'Name': 'URL','Value': URLfromTable}],Value=y)
    Metric2=Health1.putData(NAMESPCAE,Metricname='Health',Dimention=[{'Name': 'UR','Value': URLfromTable}],Value=x)  
    gbvars.URL1=URLfromTable
    print(gbvars.URL1)
    print(Metric1,Metric2)                       
    return [x,y]
    
                             
def latency(url:str):
    x = datetime.datetime.now()
    start=x.strftime("%f")
    #print(start)
    http = urllib3.PoolManager()
    r=http.request('GET',url)
    y = datetime.datetime.now()
    end =y.strftime("%f")
    #print(end)
    latencytime=abs(int(start)-int(end))
    result=latencytime*(0.000001)  
    return result
    
def healthchk(url:str):
    http = urllib3.PoolManager()
    r=http.request('GET',url)   
    if r.status ==200:
        return 1
    else:
        return 0

def getTableData():
    #tname=os.environ['TABLE_NAME']
    dynamodbTable = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodbTable.Table('Week4SprintStack-TableforURLs91F16768-6P5L6XZNU1Y')
   
    response=table.scan()
   
    URLs_to_Monitor = response['Items']
    URL_Sorted_Time=sorted(URLs_to_Monitor,key=itemgetter('Time'))
    Latest_Item=URL_Sorted_Time[-1]
    
    URL_Latest=Latest_Item["url_name"]
    
    
    
    return URL_Latest
    
    
 