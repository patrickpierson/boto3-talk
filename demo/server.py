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
