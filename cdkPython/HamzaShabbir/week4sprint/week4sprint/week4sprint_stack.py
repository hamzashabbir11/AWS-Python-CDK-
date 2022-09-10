from aws_cdk import (
    # Duration,
    Duration, Stack,RemovalPolicy, aws_events as events_, aws_events_targets as targets_,
    aws_lambda as lambda_,aws_cloudwatch as cloudwatch_,aws_iam as iam_, aws_sns as sns_,
    aws_sns_subscriptions as snssubs_,aws_cloudwatch_actions as cw_actions_,aws_dynamodb as ddb_,aws_apigateway as apigateway_
)
    # aws_sqs as sqs,
from constructs import Construct
from resources import globalvars
import os
#tname=os.environ.get('TABLE_NAME')
class Week4SprintStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        #Creating Lamda and Assigning Role to it 
        lamrole=self.lamdarole() 
        hw_lambda=self.createfunc("MyLambda","./resources","hw_lambda.LambdaHandler",lamrole)
        sns_lambda=self.createfunc("alarmlambda","./resources","sns_lamda.AlarmLamda",lamrole)
             
        api_lambda=self.createfunc("APILambdafunction","./resources","api_lambda.api_handler",lamrole)

        #creating API Gateway
        #https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_apigateway.html
        myapi=apigateway_.LambdaRestApi(self,"HamzaShabbir_API",handler=api_lambda,proxy=False)
        resource=myapi.root.add_resource("urls")
        integtation=apigateway_.LambdaIntegration(api_lambda)
        
        #content_handling=apigateway_.ContentHandling.CONVERT_TO_TEXT
        apigateway_.LambdaRestApi
       
        #Adding API Methods
        resource.add_method("GET",integration=integtation,authorization_type=apigateway_.AuthorizationType.NONE,
        api_key_required=False)

        resource.add_method("POST",integration=integtation,authorization_type=apigateway_.AuthorizationType.NONE,
        api_key_required=False)

        #resource.add_method("PUT",integration=integtation,authorization_type=apigateway_.AuthorizationType.NONE,
        #api_key_required=False)

        resource.add_method("DELETE",integration=integtation,authorization_type=apigateway_.AuthorizationType.NONE,
        api_key_required=False)
        

        #Creting Table to Store 
        Table_url=ddb_.Table(self, id="Table for URLs",
        partition_key=ddb_.Attribute(name="url_name", type=ddb_.AttributeType.STRING),
        sort_key=ddb_.Attribute(name='Time',type=ddb_.AttributeType.STRING))
        
        Table_url.grant_full_access(api_lambda)
        tname=Table_url.table_name
        api_lambda.add_environment(key="TABLE_NAME",value=tname)
        
        api_lambda.apply_removal_policy(RemovalPolicy.DESTROY)


                 
        mytable=self.createTable()
        mytable.grant_full_access(sns_lambda)  
        tname=mytable.table_name

        sns_lambda.add_environment(key="TABLE_NAME", value=tname)


        # Scheduling a Cron Job, Adding Lambda as Target and defining Rule
        schedule=events_.Schedule.rate(Duration.minutes(1))
        target=targets_.LambdaFunction(handler=hw_lambda)  
        #target2=targets_.LambdaFunction(handler=sns_lambda)             
        rule = events_.Rule(self, "rule_new", 
        schedule=schedule,
        targets=[target])

        
        #Creting Cloud Watch Metrics for Latency
        dimentions={'URL': globalvars.URL1}
        metric=cloudwatch_.Metric(
        namespace=globalvars.NAMESPCAE,
        metric_name='Latency',
        dimensions_map=dimentions,
        period=Duration.minutes(1),
        label='Latency')  

        


        #Creating Alarm and Raising alarm on Latency
        latencyalarm = cloudwatch_.Alarm(self, "Alarm_Hamza",
        comparison_operator=cloudwatch_.ComparisonOperator.GREATER_THAN_THRESHOLD,
        threshold=0.4,
        evaluation_periods=1, datapoints_to_alarm=1,
        metric=metric
                    )

        #https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_cloudwatch_actions/SnsAction.html
        mytopic=sns_.Topic(self,id="hamzatopic")
        latencyalarm.add_alarm_action(cw_actions_.SnsAction(mytopic))
        # Error was www in url was missing  
        
        #https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_sns/Topic.html
        #https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_dynamodb/Table.html
       
      
       
        # Creting SNS Topic and Subscrbing email to it.
    
        
        mytopic.add_subscription(snssubs_.EmailSubscription('hamzashabbir447@gmail.com'))
        mytopic.add_subscription(snssubs_.LambdaSubscription(sns_lambda))
        

    def createfunc(self,id_,path,handler,lamrole):
        
        return lambda_.Function(self, id_,
        code=lambda_.Code.from_asset(path),
        handler=handler,
        runtime=lambda_.Runtime.PYTHON_3_8,role=lamrole)

    def lamdarole(self):
        lambda_role = iam_.Role(self,"rolehamzashabs",
        assumed_by=iam_.ServicePrincipal("lambda.amazonaws.com"),
        description="Example role db"
        )        
        lambda_role.add_managed_policy(iam_.ManagedPolicy.from_aws_managed_policy_name("CloudWatchFullAccess"))
        lambda_role.add_managed_policy(iam_.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess"))
        lambda_role.add_managed_policy(iam_.ManagedPolicy.from_aws_managed_policy_name("AmazonAPIGatewayInvokeFullAccess"))
        return lambda_role

    def createTable(self):
        return ddb_.Table(self, id="Hamza Table",
        partition_key=ddb_.Attribute(name="msgid", type=ddb_.AttributeType.STRING))


