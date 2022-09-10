import boto3

class dynamo():
    def __init__(self) -> None:
        self.client=boto3.client('dynamodb')