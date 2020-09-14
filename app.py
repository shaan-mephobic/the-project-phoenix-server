from flask import Flask, request, abort, jsonify,render_template
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

#cutOffFrequency = 100.0

@app.route("/program",methods=["POST","GET"])
def fucking_shit():
    return "NONE"
    if request.method == 'POST':  
        f = request.files['file']
        filePath = "./zoomering/"+secure_filename(f.filename)
        f.save(filePath)
        aio.fname=filePath
        return "success"
        

@app.route("/")
def return_file():
    good = open(outcsv, "r+")
    return good.read()

@app.route("/isitrunning")
def run():
    return "Yeah Bitch It is Runnning, don't let it run away bruh!!!"


if __name__ == '__main__':
    app.run()
