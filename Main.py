import datetime
import moviepy.editor as mpe
import sounddevice as sound
from scipy.io.wavfile import write
import wavio as wv
from PIL import ImageGrab
from win32api import GetSystemMetrics
import numpy as np
import cv2
timeStamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M')
fileName = f'{timeStamp}.mp4'
#audioName = f'{timeStamp}.wav'
webcam = cv2.VideoCapture(0)
#freq = 44100
#print("Type in the duration of the audio recording -->     ")
#duration = 10
#recording = sound.rec(int(duration * freq), samplerate=freq, channels=2)
#sound.wait()
#write(audioName, freq, recording)
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
capturedVideo = cv2.VideoWriter(fileName, fourcc, 12.5, (width, height))
while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    _, frame = webcam.read()
    cv2.imshow('Screen Capture', img_final)
    fr_height, fr_width, _ = frame.shape
    img_final[0:fr_height, 0: fr_width, :] = frame[0:fr_height, 0: fr_width, :]
    capturedVideo.write(img_final)
    if cv2.waitKey(1) == ord('+'):
        clip = mpe.VideoFileClip(fileName)
        mic = mpe.AudioFileClip("LOCA.mp3")
        final_audio = mpe.CompositeAudioClip([mic])
        final_clip = clip.set_audio(final_audio)
        final_clip.write_videofile(f'{timeStamp} final.mp4')
        break
