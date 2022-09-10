import aws_cdk as core
import aws_cdk.assertions as assertions

from week1sprint.week1sprint_stack import Week1SprintStack

# example tests. To run these tests, uncomment this file along with the example
# resource in week1sprint/week1sprint_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Week1SprintStack(app, "week1sprint")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
