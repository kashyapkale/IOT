import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(40, GPIO.OUT)         #LED output pin
GPIO.setup(35, GPIO.OUT) 
while True:
    i=GPIO.input(8)
    if i==0:                 #When output from motion sensor is LOW
        print("No MOTION" + str(i))
        GPIO.output(40, 0)  #Turn OFF LED
        GPIO.output(35, 0)
        time.sleep(2)
    elif i==1:               #When output from motion sensor is HIGH
        print("MOTION detected" + str(i))
        GPIO.output(40, 1)  #Turn ON LED
        GPIO.output(35, 1)
        time.sleep(1)
    GPIO.output(40, 0)
    GPIO.output(35, 0)
    time.sleep(1)