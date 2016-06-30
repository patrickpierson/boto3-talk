import boto3, time, StringIO
from SimpleCV import Image, Camera

loop = True

while loop == True:
  user_input = raw_input('Take a picture by typing "cheese" or exit by typing "exit": ')
  
  if user_input == 'cheese':
    output = StringIO.StringIO()
    time_now = int(time.time())
    cam = Camera()
    img = cam.getImage()
    img.save(output.write())
    print output

  if user_input == 'exit':
    break
