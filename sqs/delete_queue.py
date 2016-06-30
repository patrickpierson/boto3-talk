import boto3, sys

sqs = boto3.client('sqs')

response = sqs.delete_queue(QueueUrl=sys.argv[1])

print(response)

