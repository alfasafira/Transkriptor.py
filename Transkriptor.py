from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import tkinter
from tkinter import * 
from tkinter.ttk import * 
from tkinter.messagebox import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename  
from tkinter.filedialog import askdirectory
import os
import sys

apikey = 'eottaCZFoKcszVt1Q0hX5SE06UZ59JpyV0-uqKHDmyF_'
url = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com/instances/7f2f119c-caeb-460e-a1e1-9f6e0561437d'
authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

def Import_File():
    filename = filedialog.askopenfilename()
    with open(filename, 'rb') as f:
        res = stt.recognize(audio=f, content_type='audio/mp3', model='en-US_NarrowbandModel', continuous=True).get_result()
        text = res['results'][0]['alternatives'][0]['transcript']
    return text

def Do():
    text = Import_File()
    tempat = askdirectory(initialdir='/', title='Select Folder')
    file = open(tempat+'/Output.txt', 'w')
    file.write(text)

root = Tk()  
root.title("Transkriptor") 
root.geometry("300x150") 
root.resizable(False, False)  
label = Label(root, text="Pilih File Audio(.mp3) beserta Folder Outputnya") 
label.place(relx=0.5, rely=0.2, anchor=CENTER)
button = Button(root, text="Pilih", command=Do) 
button.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()