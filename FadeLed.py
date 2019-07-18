import RPi.GPIO as GPIO   
import time               

GPIO.setmode(GPIO.BCM) 
                         

GPIO.setup(18, GPIO.OUT)  
pwm = GPIO.PWM(18, 100)   

dc=0                             
pwm.start(dc)                      
while True:                      
    for dc in range(0, 101, 5):    
      pwm.ChangeDutyCycle(dc)
      time.sleep(0.1)             
      print(dc)
    for dc in range(95, 0, -5):    
      pwm.ChangeDutyCycle(dc)
      time.sleep(0.1)             
      print(dc)
      
pwm.stop()                         
GPIO.cleanup()  

