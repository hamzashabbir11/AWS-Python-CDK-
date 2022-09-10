import aws_cdk as core
from aws_cdk import Stack
import aws_cdk.assertions as assertions
from aws_cdk.assertions import Template
from week3sprint.week3sprint_stack import Week3SprintStack
#https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.assertions/README.html

# example tests. To run these tests, uncomment this file along with the example
# resource in week3sprint/week3sprint_stack.py
def test_lambda_count():
    app = core.App()
    stack = Week3SprintStack(app, "week3sprint")
    template = assertions.Template.from_stack(stack)
    template.resource_count_is("AWS::Lambda::Function", 2)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })

# I got this pytest error
#https://stackoverflow.com/questions/35045038/how-do-i-use-pytest-with-virtualenv