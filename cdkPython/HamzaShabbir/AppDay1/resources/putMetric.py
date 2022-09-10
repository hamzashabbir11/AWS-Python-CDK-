import boto3
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html#CloudWatch.Client.put_metric_data

class putMetriCloudWatch:
    def __init__(self) -> None:
        self.client=boto3.client('cloudwatch')
        
    
    def putData(self,Namespace,Metricname,Dimention,Value):
        response=self.client.put_metric_data(
        Namespace=Namespace,
        MetricData=[
            {
                'MetricName': Metricname,
                'Dimensions': Dimention,
                'Value': Value,
            },
        
            ]            
        
    )
        
        
        

