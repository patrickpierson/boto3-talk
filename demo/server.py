import boto3, time, os
from SimpleCV import Image, Camera

time_now = int(time.time())
filename = '%s.jpg' % time_now
cam = Camera()
img = cam.getImage()
img.save(filename)

s3 = boto3.resource('s3')
response = s3.Object('python-frederick-demo', filename).put(Body=open(filename, 'rb'))
print response

os.remove(filename)

sqs = boto3.resource('sqs')

queue = sqs.get_queue_by_name(QueueName='demo')

response = queue.send_message(MessageBody=filename, MessageAttributes={
         'Bucket': {
                     'StringValue': 'python-frederick-demo',
                     'DataType': 'String'
                 }})

print('MessageId: ' + response.get('MessageId'))
print('MD5: ' + response.get('MD5OfMessageBody'))
