import boto3
s3 = boto3.resource('s3')

# Create the bucket named python-frederick
response = s3.create_bucket(Bucket='python-frederick')

# Print response from creation
print response
