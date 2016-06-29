import boto3

sqs = boto3.resource('sqs')

for queue in sqs.queues.all():
    print(queue.url)
