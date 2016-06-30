import boto3

s3 = boto3.resource('s3')

# Put the test.txt object into the python-frederick object
response = s3.Object('python-frederick', 'test.txt').put(Body=open('./test.txt', 'rb'))

print response
