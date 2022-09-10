import aws_cdk as cdk
from aws_cdk import (
    # Duration,
    Duration, SecretValue, Stack,RemovalPolicy, Stage, aws_events as events_, aws_events_targets as targets_,
    aws_lambda as lambda_,aws_cloudwatch as cloudwatch_,aws_iam as iam_, pipelines as pipeline_,
    aws_codepipeline_actions as codepipeactions_   
)

from constructs import Construct
from week3sprint.pipelineStage import HamzaStage1

class Hamzapipleline3(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        source=pipeline_.CodePipelineSource.git_hub("hamzashabbir2022skipq/Pegasus_Python","main",
        authentication=SecretValue.secrets_manager('mysecret'),
        trigger=codepipeactions_.GitHubTrigger.POLL)

        build=pipeline_.ShellStep("Synth",
            input=source,
            commands=['cd HamzaShabbir/week3sprint/', 'npm install -g aws-cdk', 'python -m pip install -r  requirements.txt' ,'cdk synth'],
            primary_output_directory='HamzaShabbir/week3sprint/cdk.out'
        )

        pipeline = pipeline_.CodePipeline(self, "MyPipelineHamzaShabbir",
        synth=build)
    

        #https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.core/Stage.html

        betatest=pipeline_.ShellStep('Unit Test',
        commands=['cd HamzaShabbir/week3sprint/','pip install pytest','npm install -g aws-cdk',
        'python -m pip install -r  requirements.txt','pytest' ],
        input=source)
        beta = HamzaStage1(self, "BetaStage")
        #beta=cdk.Stage(self,'betastage')
        pipeline.add_stage(beta,pre=[betatest])

        prod = HamzaStage1(self, "Prod")
      
        pipeline.add_stage(prod,
        pre=[
            pipeline_.ManualApprovalStep("PromoteToProd")
        ]
    )
       
        
        
              
    
#https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html      
        
        





