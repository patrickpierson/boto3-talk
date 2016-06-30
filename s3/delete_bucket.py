import boto3
s3 = boto3.resource('s3')

bucket = s3.Bucket('python-frederick')

# Print bucket info on python-frederick
print bucket

# Cycle through the key names for objects and delete them
for key in bucket.objects.all():
  print key.delete()

# Print and delete the bucket
print bucket.delete()
