from flask import Flask, request,redirect,send_file,url_for,send_from_directory, abort, jsonify,render_template
import numpy as np
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import wave
import subprocess
import aio
import math
import contextlib
from pydub import AudioSegment
import os
import matplotlib.pyplot as plt
import sys

owe = 1
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['wav','mp3','flac','aac'])
filename = ''
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
        #if file and allowed_file(file.filename):

        print ('**found file', file.filename)
        rite=open("data.csv","a")
        rite.write(file.filename+"\n")
        rite.close()
        filename = secure_filename(file.filename)
        file.save(filename)

        
        extension = filename.split(".")[-1]
        if extension =='mp3':
            dst = "mp3ed.wav"
            mpier = AudioSegment.from_mp3(filename)
            mpier.export("mp3ed.wav",format="wav")
            print("here")
            
            aio.fname = dst
            aio.io()
            os.remove(filename)
            os.remove(dst)
            #return send_file('darted.csv', mimetype= 'text/json',attachment_filename='darted.csv',
                     #as_attachment=True)
        if extension =='flac':
            dst = "fltow.wav"
            mpier = AudioSegment.from_file(filename)
            mpier.export(dst,format="wav")
            print("here")
            
            aio.fname = dst
            aio.io()
            os.remove(filename)
            os.remove(dst)
            #return send_file('darted.csv', mimetype= 'text/json',attachment_filename='darted.csv',
                     #as_attachment=True)

        if extension =='m4a':
            dst = "m4aluv.wav"
            mpier = AudioSegment.from_file(filename)
            mpier.export(dst,format="wav")
            print("here")
            
            aio.fname = dst
            aio.io()
            os.remove(filename)
            os.remove(dst)
            #return send_file('darted.csv', mimetype= 'text/json',attachment_filename='darted.csv',
                     #as_attachment=True)

        if extension =='aac':
            dst = "mp3ed.wav"
            mpier = AudioSegment.from_file(filename)
            mpier.export("mp3ed.wav",format="wav")
            print("here")
            
            aio.fname = dst
            aio.io()
            os.remove(filename)
            os.remove(dst)
            #return send_file('darted.csv', mimetype='text/json',attachment_filename='darted.csv',
                     #as_attachment=True)
        if extension == "wav":
            aio.fname = filename
            aio.io()
            os.remove(filename)
            #return send_file('darted.csv',mimetype='text/json',attachment_filename='darted.csv',
                     #as_attachment=True)

        print("sent")
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

@app.route("/sagan")
def saganer():
    return send_file('darted.csv', mimetype= 'text/json',attachment_filename='darted.csv',
                    as_attachment=True)
                    
@app.route("/isitrunning")
def run():
    return "Yeah It's Running, You Can't Outrun It!"

@app.route("/showdata")
def dataret():
    dat = open("data.csv", "r")
    return dat.read()

@app.route("/downloadata")
def downdata():
    return send_file('data.csv', mimetype= 'text/json',attachment_filename='fulldata.csv',
                    as_attachment=True)

if __name__ == '__main__':
	app.run(threaded = True)