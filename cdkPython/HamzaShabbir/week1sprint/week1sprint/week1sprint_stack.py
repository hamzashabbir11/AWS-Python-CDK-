from constructs import Construct
from aws_cdk import (
    # Duration,
    RemovalPolicy, Stack,aws_lambda as lambda_ ,
    aws_events as events_,
    aws_events_targets as targets_
    # aws_sqs as sqs,    
)
from constructs import Construct
#import requests
import datetime 
import urllib3

class Week1SprintStack(Stack):
   
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        hw_lambda=self.createfunc("MyLambda","./resources","hw_lambda.LambdaHandler")
        hw_lambda.apply_removal_policy(RemovalPolicy.DESTROY)
        schedule=events_.Schedule.cron(minute="1")
        target=targets_.LambdaFunction(handler=hw_lambda)        
        rule = events_.Rule(self, "rule", 
        schedule=schedule,
        targets=[target])               
        rule.add_target(targets_.LambdaFunction(hw_lambda))
        
    def createfunc(self,id_,path,handler):
        return lambda_.Function(self, id_,
        code=lambda_.Code.from_asset(path),
        handler=handler,
        runtime=lambda_.Runtime.PYTHON_3_8)
                
        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "Week1SprintQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
