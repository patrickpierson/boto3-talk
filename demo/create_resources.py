import boto3

sqs = boto3.resource('sqs')
queue = sqs.create_queue(QueueName='demo', Attributes={'DelaySeconds': '5'})

s3 = boto3.resource('s3')
response = s3.create_bucket(Bucket='python-frederick-demo')

