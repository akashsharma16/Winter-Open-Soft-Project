from flask import Flask, redirect, url_for, request,render_template
import os
from pathlib import Path
import boto3

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   #path = Path(name)
   imageFile = name
   client = boto3.client('rekognition')

   with open(imageFile, 'rb') as image:
      response = client.detect_text(Image={'Bytes': image.read()})

   uniquetext = set()

   for text in response['TextDetections']:
      uniquetext.add(text['DetectedText'])

   returnedtext = ""

   #print('Detected text in ' + imageFile)
   # for text in response['TextDetections']:
   #    print(text['DetectedText'] + ' : ' + str(text['Confidence']))

   for i in uniquetext:
      returnedtext += i + " "


   return returnedtext

@app.route('/login', methods=['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success', name=user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success', name=user))

if __name__ == '__main__':
      app.run(debug=True)
