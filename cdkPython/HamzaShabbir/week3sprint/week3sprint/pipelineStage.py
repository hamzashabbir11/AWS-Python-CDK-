from aws_cdk import (
    # Duration,
    Duration, Stage,RemovalPolicy, aws_events as events_, aws_events_targets as targets_,
    aws_lambda as lambda_,aws_cloudwatch as cloudwatch_,aws_iam as iam_, 
)
import aws_cdk as cdk
    
from constructs import Construct
from week3sprint.week3sprint_stack import Week3SprintStack


class HamzaStage1(Stage):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.stage=Week3SprintStack(self,"HamzaStack")
       