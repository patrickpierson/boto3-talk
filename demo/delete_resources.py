import boto3

sqs = boto3.client('sqs')
response = sqs.delete_queue(QueueUrl='https://queue.amazonaws.com/########/demo')

s3 = boto3.resource('s3')
bucket = s3.Bucket('python-frederick-demo')

for key in bucket.objects.all():
      print key.delete()

print bucket.delete()

