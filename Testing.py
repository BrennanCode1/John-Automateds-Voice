import os
import time
import pyautogui 
import simpleaudio as sa
import sounddevice as sd


callN=0 
print(pyautogui.size()) 

while callN < 101 :
    callN+=1
    #intiializeing code to answer phone call
    #intislizing code to check if phone call answered
    #check the number is 1 on the first call
    if callN == 1:
        print("Playing Recording for voice 1")
        #do the automated voice
        #check if voice call automation is over
        #hang up phone call
        wave_obj = sa.WaveObject.from_wave_file("/Users/brennan1/Downloads/fuckoff.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done() 
        print("Recording over moving to caller 2")
    elif callN == 2:
        print("2")
        #do the automated voice
        #check if voice call automaiton is over
        #hang up phone call
    elif callN==3:  
        print ("3")
    #adding one to the count to loop again for the next call
    #check if phone is hung up
    #add alert if code breaks
