#!/usr/bin/env python


import socket
import os
import Motor

UDP_IP = ''
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print "Listening on UDP PORT %s" %UDP_PORT


while(1):

        sockdata, addr = sock.recvfrom(64) # buffer size is 64 bytes
        if sockdata[0] == 'D':
            print "DC Motor"
            DCCommand = sockdata.split(',')
            #print "%d %d %d" % (int(DCCommand[1]), int(DCCommand[2]),int(DCCommand[3])) 
            Motor.moveDCMotor(int(DCCommand[1]), int(DCCommand[2]),int(DCCommand[3]))
            #time.sleep(0.1)
        elif sockdata[0] == 'S':
            print "Servo Motor"
            ServoCommand = sockdata.split(',')
            Motor.moveServoMotor(int(ServoCommand[1]))
            #time.sleep(0.1)
	
	#print sockdata
	#connection.close()



