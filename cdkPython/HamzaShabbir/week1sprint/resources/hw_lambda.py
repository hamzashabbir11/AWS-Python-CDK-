import datetime
#import requests
import urllib3

URL1="http://skipq.org"
def LambdaHandler(event,context):
    x=healthchk()
    y=latency()
    print("Hello I'm Still Here")
    return (x,y)
   
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
    healthy=healthchk()
    print(result,healthy)
    return result,healthy
    
def healthchk():
    http = urllib3.PoolManager()
    r=http.request('GET',URL1)   
    if r.status ==200:
        return True 
    else:
        return False


