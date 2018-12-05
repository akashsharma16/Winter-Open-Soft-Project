"""
import boto3

if __name__ == "__main__":

    imageFile = r'C:\Users\vandi\Desktop\coffee.jpg'
    client = boto3.client('rekognition')

    with open(imageFile, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})

    print('Detected labels in ' + imageFile)
    for label in response['Labels']:
        print(label['Name'] + ' : ' + str(label['Confidence']))

    print('Done...')

"""

import boto3

if __name__ == "__main__":

    bucket = 'bucket'
    photo = 'inputtext.jpg'

    client = boto3.client('rekognition')

    response = client.detect_text(Image={'S3Object': {'Bucket': bucket, 'Name': photo}})

    textDetections = response['TextDetections']
    print
    response
    print
    'Matching faces'
    for text in textDetections:
        print
        'Detected text:' + text['DetectedText']
        print
        'Confidence: ' + "{:.2f}".format(text['Confidence']) + "%"
        print
        'Id: {}'.format(text['Id'])
        if 'ParentId' in text:
            print
            'Parent Id: {}'.format(text['ParentId'])
        print
        'Type:' + text['Type']
        print