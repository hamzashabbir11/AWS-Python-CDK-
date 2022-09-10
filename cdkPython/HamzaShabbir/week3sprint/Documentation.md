# CI/CD on AWS Using AWS Developer Tools

### API Reference 
- <a href="https://aws.amazon.com/codepipeline/">AWS Code Pipelines</a>
  1. <a href=https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.pipelines/CodePipelineSource.html>Source</a> <br>
  2. [Build using ShellStep](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.pipelines/ShellStep.html) <br>
  3. [PipeLine Stage](https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.core/Stage.html)  
- [Manual Approval Step](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.pipelines/ManualApprovalStep.html)
- [AWS Code Deploy- Lamda Deployment Group](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_codedeploy/LambdaDeploymentGroup.html)
  1. [Deployment Configuration](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_codedeploy/LambdaDeploymentConfig.html)


### Project Workflow 
1. Define a source from Github. 
2. Build The Code Using Shell Step 
3. Beta Testing Stage for Unit Tests
4. Finnaly a Manual Approval Step befroe deployment to Deployment Groups
