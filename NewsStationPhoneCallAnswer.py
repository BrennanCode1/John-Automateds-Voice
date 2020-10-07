import os
import time
import pyautogui 
import simpleaudio as sa
import sounddevice as sd


callN=0 
print(pyautogui.size()) 

while callN < 101 :
    callN+=1
    #code to answer phone call
    #Johns Screen size to click on call
    print("Playing Recording for voice"+callN)
    #do the automated voice
    wave_obj = sa.WaveObject.from_wave_file("/Users/brennan1/Downloads/JohnsPhoneCall"+callN+".wav")
    play_obj = wave_obj.play()
    #check if voice call automation is over
    play_obj.wait_done() 
    #hang up phone call
    print("Recording over moving to next caller")
