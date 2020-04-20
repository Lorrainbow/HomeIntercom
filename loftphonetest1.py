import os
from gpiozero import Button
from time import sleep

buttonOne = Button(18)
buttonTwo = Button(15)
buttonThree = Button(14)
volumeButton = Button(16)
ringerButton = Button(12)

def ringerOn():	
	os.system("mumble rpc unmute")
def ringerOff():	
	os.system("mumble rpc mute")
def volumeOn():
	os.system("mumble rpc undeaf")
def volumeOff():
	os.system("mumble rpc deaf")

while True:
    if buttonOne.is_pressed:               
        #turn the speaker & the microphone on        
        os.system("mumble rpc undeaf")	
        #ring the bell
        os.system("sudo python ringbell.py")
		
    ringerButton.when_pressed = ringerOff
    ringerButton.when_released = ringerOn
    volumeButton.when_pressed = volumeOn
    volumeButton.when_released = volumeOff	

    sleep(0.3)