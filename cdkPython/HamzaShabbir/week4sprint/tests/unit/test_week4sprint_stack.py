import aws_cdk as core
import aws_cdk.assertions as assertions

from week4sprint.week4sprint_stack import Week4SprintStack

# example tests. To run these tests, uncomment this file along with the example
# resource in week4sprint/week4sprint_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Week4SprintStack(app, "week4sprint")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
