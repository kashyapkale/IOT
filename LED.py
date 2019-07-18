import RPi.GPIO as a
import time
a.setmode(a.BCM)
a.setwarnings(False)
a.setup(18,a.OUT)
a.setup(21,a.OUT)

while True :
        a.output(21,a.LOW)
        a.output(18,a.LOW)
        time.sleep(2) 
        a.output(21,a.HIGH)
        time.sleep(2)
        a.output(18,a.HIGH)
        a.output(21,a.LOW)
        time.sleep(2)
        a.output(21,a.HIGH)
        time.sleep(2)
       
    
