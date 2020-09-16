from flask import Flask, request,redirect, abort, jsonify,render_template
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

app = Flask(__name__)
# inputter = 'C:/Users/shaan/Music/drowningdart.wav'
outcsv = 'darted.csv'

#fname = 'C:/Users/shaan/Music/drowningdart.wav'
#outname = 'darted.wav'
@app.route('/',methods=["POST","GET"])  
def upload():  
    return render_template("file_upload_form.html")  
@app.route('/success',methods=["POST","GET"])
def fuckingshit():
    if request.method == 'POST':  
        f = request.files['file']  
        
        filepath = "./zoomer/"+secure_filename(f.filename)  
        
        
        f.save(filepath)  
        print (filepath)   
        aio.fname=filepath
        print(aio.fname)
        aio.Jupiter.io()
       # aio.fname=filepath
        os.remove(filepath)
      #  aio.fname = rowdy
        return render_template("success.html", name = f.filename) 
        

    #if request.method == 'POST':  
    #    f = request.files['file']
    #    filePath = "./zoomering/"+secure_filename(f.filename)
    #    f.save(filePath)
    #    aio.fname=filePath
    #    return "success"
        

@app.route("/output")
def return_file():
    good = open(outcsv, "r")
    return good.read()

@app.route("/isitrunning")
def run():
    return "Yeah Bitch It is Runnning, don't let it run away bruh"


if __name__ == '__main__':
    app.run()
