from flask import Flask, request
import json
import urllib.parse
import os

app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

@app.route('/getAudio', methods=['GET'])
def getAudio():
    file = request.args.get('name')
    if os.path.exists(file):
        with open(file, 'rb') as fobj:
            return fobj.read()
    else:
        return "File not found", 404

@app.route('/storeAudio', methods=['POST'])
def storeAudio():
    if 'fieldname' not in request.files:
        return 'No file part'

    file = request.files['fieldname']

    if file.filename == '':
        return 'No selected file'

    if file:
        # You can now process the uploaded file. For example, you can save it to the server:
        file.save('./uploaded_audio.wav')
        return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)