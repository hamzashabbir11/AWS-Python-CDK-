import datetime
import urllib3
import boto3,putmetricClass
URL1="http://www.skipq.org"
NAMESPCAE='HAMZASHABBIRWEBHEALTH'
import globalvars as gbvars
# boto3 documentaation 
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_data
def LambdaHandler(event,context):
    x=healthchk()
    y=latency()
    print("Hello I'm Still Here",x,y)
    Latency1=putmetricClass.putMetriCloudWatch()
    Health1=putmetricClass.putMetriCloudWatch()
    Metric1=Latency1.putData(NAMESPCAE,Metricname='Latency',Dimention=[{'Name': 'URL','Value': gbvars.URL1}],Value=y)
    Metric2=Health1.putData(NAMESPCAE,Metricname='Health',Dimention=[{'Name': 'UR','Value': gbvars.URL1}],Value=x)  
    print(Metric1,Metric2)                          
    return [x,y]
    
                             
def latency():
    x = datetime.datetime.now()
    start=x.strftime("%f")
    #print(start)
    http = urllib3.PoolManager()
    r=http.request('GET',URL1)
    y = datetime.datetime.now()
    end =y.strftime("%f")
    #print(end)
    latencytime=abs(int(start)-int(end))
    result=latencytime*(0.000001)  
    return result
    
def healthchk():
    http = urllib3.PoolManager()
    r=http.request('GET',URL1)   
    if r.status ==200:
        return 1
    else:
        return 0

