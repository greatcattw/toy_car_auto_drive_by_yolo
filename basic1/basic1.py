from ultralytics import YOLO
from PIL import Image
import cv2
import numpy as np
import sys
import os
import csv
import serial
import time
import keyboard
import sys, tty, termios, threading, time

# y8_bw2.py

def chk_rr():
  ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)

  cmd=b"C"
  write_len = ser.write(cmd)
  time.sleep(0.3)
  write_len = ser.write(b"Z")
  ser.close()
  time.sleep(0.5)
  
def stop():
  ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)
                                  
  cmd=b"Z"     
  write_len = ser.write(cmd) 
  
  
  ser.close()
#---
def jog():
  ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)
                                  
  cmd=b"A"     
  write_len = ser.write(cmd) 
  #time.sleep(0.5)
  #write_len = ser.write(b"Z")

  ser.close()
#---
def trun_r():
  ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)

  cmd=b"C"
  write_len = ser.write(cmd)
  time.sleep(0.1)
  #write_len = ser.write(b"Z")
  write_len = ser.write(b"A")
  
  ser.close()
#---
def trun_l():
  ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)
 
  cmd=b"G"
  write_len = ser.write(cmd)
  time.sleep(0.1)
  #write_len = ser.write(b"Z")  
  write_len = ser.write(b"A")  

  ser.close()
#---
'''
def trun_rr():
  ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)

#  cmd=b"\x01\x64\x02\x73\x03"     
#  write_len = ser.write(cmd)      
                                  
#  for i1 in range(50):            
#    write_len = ser.write(b"\x01")

  cmd=b"\x01\x64\x02\x6f\x03"
  write_len = ser.write(cmd)

  ser.close()
#---
def trun_ll():
  ser = serial.Serial(port="/dev/ttyUSB0", baudrate=9600)

#  cmd=b"\x01\x73\x02\x64\x03"     
#  write_len = ser.write(cmd)      
                                  
#  for i1 in range(50):            
#    write_len = ser.write(b"\x01")  
  
  cmd=b"\x01\x6f\x02\x64\x03"
  write_len = ser.write(cmd)

  ser.close()
#---
'''
def dicision_execution():
  f1='result.csv'   
  lines = len(open(f1).readlines())
  #print('The total lines is ',lines)
  if (lines == 0):
    ret=4
    print("----------------------")
    chk_rr()
    ##stop()
  else:

    max_y=-9999
    with open('result.csv', newline='') as csvfile:
      rows = csv.reader(csvfile)
      for row in rows:
       # print(row[1])
        if (int(row[1])>max_y):
          max_y=int(row[1])
          max_row=row
#print(max_y)
#print(max_row)

    ret=2
    #centerline=1280/2
    centerline=840
    
    tolrence=50
    box_c=int( (int(max_row[0])+int(max_row[2])) / 2 )
#    print("=============================",box_c)
    if (int(box_c) < (centerline-tolrence)):
      ret=1
      print("LLLLLLLLLLLLLLLLLLLLLLL ",box_c)      
      trun_l()

    if (int(box_c) > (centerline+tolrence)):
      ret=3
      print("RRRRRRRRRRRRRRRRRRRRRRR ",box_c)      
      trun_r()

    if (ret == 2):
      print("JJJJJJJJJJJJJJJJJJJJJJJ ",box_c)
      jog()
      
  print(ret)
#---

def wait_key():
  global flg_main_while
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
    tty.setraw(sys.stdin.fileno())
    ch = sys.stdin.read(1)
  finally:
    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
  flg_main_while=False
  
  
  
#---
def get_pic():
  os.system("wget http://192.168.100.1:8080/?action=snapshot -O /tmp/6.jpg")
#---
 

def auto_drive():
  fname_num=0
  while True:
    get_pic()
  
# log pic for debug 
    fname1='{0:06d}'.format(fname_num)
    fname_num=fname_num+1
    log_filename=str(fname1)+'.jpg'  
    os.system(f"cp /tmp/6.jpg log/{log_filename}");

# from PIL
    im1 = Image.open("/tmp/6.jpg")
# save=True：存檔
    results = model.predict(source=im1, save=False, save_txt=False, conf=0.7, verbose=False)


    with open("result.csv", '+w') as file:
        for idx, prediction in enumerate(results[0].boxes.xyxy): # change final attribute to desired box format
            cls = int(results[0].boxes.cls[idx].item())
          # Write line to file in YOLO label format : cls x y x y
            file.write(f"{int(prediction[0].item())},{int(prediction[1].item())},{int(prediction[2].item())},{int(prediction[3].item())},{cls}\n")
  
    dicision_execution()
#---    
def fsafe_folder():
  try:
    os.mkdir("log")
  except:
    pass  
#--- 
  
    
############ main 
print("Press any key to exit")
print("loading pt ...")
model = YOLO("AIA_XT131_01_v3.pt")
print("done\n")

fsafe_folder()

t = threading.Thread(target=auto_drive,daemon=True)
t.start()

wait_key()
    
stop()    

