from libsonyapi.camera import Camera
from libsonyapi.actions import Actions
import requests 
import time

camera = Camera()  # create camera instance
camera_info = camera.info() # get camera camera_info
delay_time=int(input("Enter delay time between photos"))
num_shots=int(input("Enter number of photos to take"))
start_time=int(input("Enter start timer"))
time.sleep(start_time)
for shot_no in range(num_shots):
    camera.do(Actions.actTakePicture)
    time.sleep(delay_time)
