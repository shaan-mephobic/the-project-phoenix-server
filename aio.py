import contextlib
import math
import os
import sys
import wave
import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment

fname = ''
outname = 'darted.wav'

cutOffFrequency = 200.0

print('fuck')

if fname !="":

    # from http://stackoverflow.com/questions/13728392/moving-average-or-running-mean
    def running_mean(x, windowSize):
        cumsum = np.cumsum(np.insert(x, 0, 0))
        return (cumsum[windowSize:] - cumsum[:-windowSize]) / windowSize


    # from http://stackoverflow.com/questions/2226853/interpreting-wav-data/2227174#2227174
    def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved=True):
        if sample_width == 1:
            dtype = np.uint8  # unsigned char
        elif sample_width == 2:
            dtype = np.int16  # signed 2-byte short
        else:
            raise ValueError("Only supports 8 and 16 bit audio formats.")

        channels = np.frombuffer(raw_bytes, dtype=dtype)

        if interleaved:
            # channels are interleaved, i.e. sample N of channel M follows sample N of channel M-1 in raw data
            channels.shape = (n_frames, n_channels)
            channels = channels.T
        else:
            # channels are not interleaved. All samples from channel M occur before all samples from channel M-1
            channels.shape = (n_channels, n_frames)

        return channels


    with contextlib.closing(wave.open(fname, 'rb')) as spf:
        sampleRate = spf.getframerate()
        ampWidth = spf.getsampwidth()
        nChannels = spf.getnchannels()
        nFrames = spf.getnframes()

        # Extract Raw Audio from multi-channel Wav File
        signal = spf.readframes(nFrames * nChannels)
        spf.close()
        channels = interpret_wav(signal, nFrames, nChannels, ampWidth, True)

        # get window size
        # from http://dsp.stackexchange.com/questions/9966/what-is-the-cut-off-frequency-of-a-moving-average-filter
        freqRatio = (cutOffFrequency / sampleRate)
        N = int(math.sqrt(0.196196 + freqRatio ** 2) / freqRatio)

        # Use moviung average (only on first channel)
        filtered = running_mean(channels[0], N).astype(channels.dtype)

        wav_file = wave.open(outname, "w")
        wav_file.setparams((1, ampWidth, sampleRate, nFrames, spf.getcomptype(), spf.getcompname()))
        wav_file.writeframes(filtered.tobytes('C'))
        wav_file.close()

    # Input audio file to be sliced
    audio = AudioSegment.from_wav("C:/Users/shaan/darted.wav", "C:/Users/shaan/test/ffmpeg.exe")

    ''' 
    Step #1 - Slicing the audio file into smaller chunks. 
    '''
    # Length of the audiofile in milliseconds
    n = 60000

    # Variable to count the number of sliced chunks
    counter = 1

    # Interval length at which to slice the audio file.
    # If length is 22 seconds, and interval is 5 seconds,
    # The chunks created will be:
    # chunk1 : 0 - 5 seconds
    # chunk2 : 5 - 10 seconds
    # chunk3 : 10 - 15 seconds
    # chunk4 : 15 - 20 seconds
    # chunk5 : 20 - 22 seconds
    interval = 10 * 10

    # Length of audio to overlap.
    # If length is 22 seconds, and interval is 5 seconds,
    # With overlap as 1.5 seconds,
    # The chunks created will be:
    # chunk1 : 0 - 5 seconds
    # chunk2 : 3.5 - 8.5 seconds
    # chunk3 : 7 - 12 seconds
    # chunk4 : 10.5 - 15.5 seconds
    # chunk5 : 14 - 19.5 seconds
    # chunk6 : 18 - 22 seconds
    overlap = 0

    # Initialize start and end seconds to 0
    start = 0
    end = 0

    # Flag to keep track of end of file.
    # When audio reaches its end, flag is set to 1 and we break
    flag = 0

    # Iterate from 0 to end of the file,
    # with increment = interval
    for i in range(0, n, interval):

        # During first iteration,
        # start is 0, end is the interval
        if i == 0:
            start = 0
            end = interval

            # All other iterations,
        # start is the previous end - overlap
        # end becomes end + interval
        else:
            start = end - overlap
            end = start + interval

            # When end becomes greater than the file length,
        # end is set to the file length
        # flag is set to 1 to indicate break.
        if end == n:
            flag = 1

        # Storing audio file from the defined start to end
        chunk = audio[start:end]

        # Filename / Path to store the sliced audio
        filename = 'chunk' + str(counter) + '.wav'

        # Store the sliced audio file to the defined path
        chunk.export(filename, format="wav")
        # Print information about the current chunk
        print("Processing chunk " + str(counter) + ". Start = "
            + str(start) + " end = " + str(end))

        # Increment counter for the next chunk
        counter = counter + 1

        # Slicing of the audio file is done.
        # Skip the below steps if there is some other usage
        # for the sliced audio files.

    with open('darted.csv', 'w+') as f:
        for i in range(1, 601):
            file = 'chunk{}'.format(i) + '.wav'
            x = AudioSegment.from_file(file)
            print(abs(x.max_dBFS), file=f)
            print(abs(x.max_dBFS))

    print("DONE BIATCH")
    for i in range(1, 601):
        os.remove("chunk{}".format(i) + '.wav')
