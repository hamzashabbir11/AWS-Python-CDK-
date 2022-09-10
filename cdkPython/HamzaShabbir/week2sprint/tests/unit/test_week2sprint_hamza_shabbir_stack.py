import aws_cdk as core
import aws_cdk.assertions as assertions

from week2sprint_hamza_shabbir.week2sprint_hamza_shabbir_stack import Week2SprintHamzaShabbirStack

# example tests. To run these tests, uncomment this file along with the example
# resource in week2sprint_hamza_shabbir/week2sprint_hamza_shabbir_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Week2SprintHamzaShabbirStack(app, "week2sprint-hamza-shabbir")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
