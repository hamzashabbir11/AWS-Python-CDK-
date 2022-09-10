import aws_cdk as core
import aws_cdk.assertions as assertions

from app_day2.app_day2_stack import AppDay2Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in app_day2/app_day2_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AppDay2Stack(app, "app-day2")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
