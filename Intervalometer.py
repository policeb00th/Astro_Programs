from libsonyapi.camera import Camera
from libsonyapi.actions import Actions
import requests 
import time
print("Connecting to camera")
camera = Camera()  # create camera instance
print("Connected to camera!!")
camera_info = camera.info() # get camera camera_info
delay_time=int(input("Enter delay time between photos:-"))
num_shots=int(input("Enter number of photos to take:-"))
start_time=int(input("Enter start timer:-"))
time.sleep(start_time)
for shot_no in range(num_shots):
    camera.do(Actions.actTakePicture)
    print(shot_no+1," photo taken out of ", num_shots)
    time.sleep(delay_time)
print("Done")