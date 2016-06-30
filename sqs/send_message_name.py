import boto3, sys

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test')

# Create a new message
response = queue.send_message(MessageBody='Testing', MessageAttributes={
    'Author': {
        'StringValue': sys.argv[1],
        'DataType': 'String'
    }})

# The response is NOT a resource, but gives you a message ID and MD5
print('MessageId: ' + response.get('MessageId'))
print('MD5: ' + response.get('MD5OfMessageBody'))
