from aws_cdk import (
    Duration,
    Stack,
    # aws_sqs as sqs,
    aws_apigateway, aws_lambda as lambda_, aws_cloudwatch as cloudwatch_, aws_cloudwatch_actions, aws_iam as iam_, aws_events as events_,
    aws_events_targets as targets_,aws_sns as sns_, aws_sns_subscriptions as sub_,
)
from constructs import Construct
url="https://naap4u78c2.execute-api.us-east-1.amazonaws.com/prod/monitor"
NAMESPACE="Hamza App 1"

class AppDay1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lamrole=self.lamdarole()
        monitor_lambda=self.createfunc("AppDay1","./resources","monitorLambda.monitorlam",lamrole)
        api_lambda=self.createfunc("ApiLambda","./resources","api_lam.apifunc",lamrole)


        myapi=aws_apigateway.LambdaRestApi(self,"app1Api",handler=api_lambda,proxy=False)
        resource=myapi.root.add_resource("monitor")
        lambda_intergation=aws_apigateway.LambdaIntegration(api_lambda)
        resource.add_method("GET",integration=lambda_intergation, authorization_type=aws_apigateway.AuthorizationType.NONE,api_key_required=False)

        schedule=events_.Schedule.rate(Duration.minutes(1))
        target=targets_.LambdaFunction(handler=monitor_lambda)       
        rule = events_.Rule(self, "rule1", 
        schedule=schedule,
        targets=[target])

         #Creting Cloud Watch Metrics for Latency
        dimentions={'Data point': url}

        metric=cloudwatch_.Metric(
        namespace=NAMESPACE,
        metric_name='Data',
        dimensions_map=dimentions,
        period=Duration.minutes(1),
        label='Data')  


        #Creating Alarm and Raising alarm on Latency
        myalarm = cloudwatch_.Alarm(self, "Alarm_Hamza",
        comparison_operator=cloudwatch_.ComparisonOperator.GREATER_THAN_THRESHOLD,
        threshold=10,
        evaluation_periods=1, datapoints_to_alarm=1,
        metric=metric)


        my_topic = sns_.Topic(self, "Topic")
        myalarm.add_alarm_action(aws_cloudwatch_actions.SnsAction(my_topic))

        my_topic.add_subscription(sub_.EmailSubscription("hamzabsee1849@gmail.com"))
        
       
       

        
                    



    def createfunc(self,id_,path,handler,lamrole):
        
        return lambda_.Function(self, id_,
        code=lambda_.Code.from_asset(path),
        handler=handler,
        runtime=lambda_.Runtime.PYTHON_3_8,role=lamrole)

    def lamdarole(self):
        lambda_role = iam_.Role(self,"app1role",
        assumed_by=iam_.ServicePrincipal("lambda.amazonaws.com"),
        description="app 1 role "
        )        
        lambda_role.add_managed_policy(iam_.ManagedPolicy.from_aws_managed_policy_name("CloudWatchFullAccess"))
        lambda_role.add_managed_policy(iam_.ManagedPolicy.from_aws_managed_policy_name("AmazonAPIGatewayInvokeFullAccess"))
        
        return lambda_role





