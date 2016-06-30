import boto3
s3 = boto3.resource('s3')

bucket = s3.Bucket('python-frederick')

print bucket

for key in bucket.objects.all():
  print key.delete()

print bucket.delete()
