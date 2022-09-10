import aws_cdk as core
import aws_cdk.assertions as assertions

from app_day1.app_day1_stack import AppDay1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in app_day1/app_day1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AppDay1Stack(app, "app-day1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
