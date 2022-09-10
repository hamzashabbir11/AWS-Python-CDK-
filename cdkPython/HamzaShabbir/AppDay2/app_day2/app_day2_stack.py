import resource
from aws_cdk import (
    # Duration,
    Stack,
    aws_apigateway as apigateway_,aws_lambda as lambda_, aws_dynamodb as ddb_, aws_iam as iam_
    # aws_sqs as sqs,
)
from constructs import Construct

class AppDay2Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        lamrole=self.lamdarole()
        event_lamda=self.createfunc("myfunc","./resources","event_lambda.eventLambda",lamrole)

        myapi1 = apigateway_.LambdaRestApi(self, "api1",
        handler=event_lamda,
        proxy=False)

        myapi2=apigateway_.LambdaRestApi(self,"api2",
        handler=event_lamda,
        proxy=False)

        integtarion=apigateway_.LambdaIntegration(event_lamda)

        resources1=myapi1.root.add_resource("val1")
        resources2=myapi2.root.add_resource("val2")

        resources1.add_method("GET",integration=integtarion,authorization_type=None,api_key_required=False)
        resources2.add_method("GET",integration=integtarion,authorization_type=None,api_key_required=False)
       
        resources1.add_method("POST",integration=integtarion,authorization_type=None,api_key_required=False)
        resources2.add_method("POST",integration=integtarion,authorization_type=None,api_key_required=False)


        mytable=ddb_.Table(self,"app2table",partition_key=ddb_.Attribute(name="value",type=ddb_.AttributeType.NUMBER),
        sort_key=ddb_.Attribute(name="Time",type=ddb_.AttributeType.STRING))
        event_lamda.add_environment(key="TABLE_NAME",value=mytable.table_name)
        mytable.grant_full_access(event_lamda)
       

        

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




    
