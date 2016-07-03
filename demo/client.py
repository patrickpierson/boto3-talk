import boto3

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='demo')

for message in queue.receive_messages(MessageAttributeNames=['Bucket']):
  print message.body
  print message.message_attributes.get('Bucket').get('StringValue')
  s3 = boto3.resource('s3')
  response = s3.Object(message.message_attributes.get('Bucket').get('StringValue'),
                       message.body).get()["Body"].read()
  #print response
  message.delete()
  fh = open(message.body, "wb")
  fh.write(str(response))
  fh.close()
