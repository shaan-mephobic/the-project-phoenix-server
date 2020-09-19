from flask import Flask, request,redirect,url_for,send_from_directory, abort, jsonify,render_template
import numpy as np
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import wave
import aio
import math
import contextlib
from pydub import AudioSegment
import os
import matplotlib.pyplot as plt
import sys

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['wav','mp3'])

app = Flask(__name__)
outcsv = 'darted.csv'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
  # this has changed from the original example because the original did not work for me
    return filename[-3:].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            print ('**found file', file.filename)
            filename = secure_filename(file.filename)
            file.save(filename)
            # for browser, add 'redirect' function on top of 'url_for'
            print (aio.fname)
            aio.fname = filename
            print (aio.fname)
            aio.io()
            os.remove(filename)    
            return url_for('uploaded_file',
                                    filename=filename)
        
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route("/output")
def return_file():
    good = open(outcsv, "r")
    return good.read()

@app.route("/isitrunning")
def run():
    return "Yeah Bitch It is Runnning, don't let it run away bruh"

if __name__ == '__main__':
	app.run()