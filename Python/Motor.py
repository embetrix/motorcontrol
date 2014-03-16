import serial
import os
import time


usbport = "/dev/ttyACM0"

motor = serial.Serial(usbport, 9600, timeout=1)

def moveServoMotor(pos):

        try:
            if (0 <= pos <= 180):
                # send 'y' character as marker for Servo Motor
                motor.write(chr(121))
                motor.write(chr(pos))
                motor.write(chr(180))
                motor.write(chr(180))
                time.sleep(0.01)
            else:
                print ("motor position is wrong !\n")
        except:
            pass

def moveDCMotor(direction, speed1, speed2):

        try:
            if (0 <= direction <= 4):
                # send 'z' character as marker for DC Motor
                motor.write(chr(122))
                motor.write(chr(direction))
                motor.write(chr(speed1))
                motor.write(chr(speed2))
                time.sleep(0.01)
            else:
                print ("motor direction is wrong !\n")
        except:
            pass


