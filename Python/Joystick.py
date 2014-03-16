#!/usr/bin/env python

import serial
import pygame
import time
import socket

# allow multiple joysticks
joy = []

xpos=0
ypos=0
speed1=0
speed2=0

# handle joystick event
def handleJoyEvent(e):
    global xpos
    global ypos
    global speed1
    global speed2

    if e.type == pygame.JOYAXISMOTION:
        axis = "unknown"
        if (e.dict['axis'] == 0):
            axis = "X"

        if (e.dict['axis'] == 1):
            axis = "Y"

        if (e.dict['axis'] == 2):
            axis = "Throttle"

        if (e.dict['axis'] == 3):
            axis = "Z"

        if (axis != "unknown"):
            str = "Axis: %s; Value: %f" % (axis, e.dict['value'])
            # uncomment to debug
            #output(str, e.dict['joy'])

            if (axis == "X" ):
                xpos = e.dict['value']
 
            if (axis == "Y" ):
                ypos = e.dict['value']


            spdy = round(ypos * 250, 0)
            speed = int(abs(spdy))
            
            if (spdy > 0):
                    direction = 2
            elif (spdy < 0):
                    direction = 1
            else:
                    direction = 4  
            
            spdx = round(xpos * 255, 0)
            delta = 150
            
            if (spdx > 150) and (speed > 150):
                    speed2 = speed
                    speed1 = speed-delta
            elif (spdx < -150) and (speed > 150):
                    speed2 = speed-delta
                    speed1 = speed
            else:
                    speed1 = speed
                    speed2 = speed
  
            print direction, speed1, speed2
            #move(direction, speed1, speed2)
            str = "%s,%s,%s,%s" % ('D', direction, speed1, speed2)
            sendCommand(str)

    elif e.type == pygame.JOYBUTTONDOWN:
        str = "Button: %d" % (e.dict['button'])
        pos=0
        # uncomment to debug
        output(str, e.dict['joy'])
        if (e.dict['button'] == 4):
            pos=0
        if (e.dict['button'] == 2):
            pos=180
        if (e.dict['button'] == 3):
           pos=90
        #moveServo(pos)
        str = "%s,%s" % ('S',pos)
        sendCommand(str)
        # Button 0 (trigger) to quit
        if (e.dict['button'] == 0):
            print "Bye!\n"
            quit()
    else:
        pass


def sendCommand(string):
    HOST, PORT = 'localhost', 1234
    UDP_IP = "192.168.1.143"
    UDP_PORT = 5005
    # SOCK_STREAM == a TCP socket
    # SOCK_DGRAM  == an UDP socket
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(string, (UDP_IP, UDP_PORT))
    except:
        pass


# print the joystick position
def output(line, stick):
    print "Joystick: %d; %s" % (stick, line)

# wait for joystick input
def joystickControl():
    while True:
        e = pygame.event.wait()
        if (e.type == pygame.JOYAXISMOTION or e.type == pygame.JOYBUTTONDOWN):
            handleJoyEvent(e)

# main method
def main():
    # initialize pygame
    pygame.joystick.init()
    pygame.display.init()
    if not pygame.joystick.get_count():
        print "\nPlease connect a joystick and run again.\n"
        quit()
    print "\n%d joystick(s) detected." % pygame.joystick.get_count()
    for i in range(pygame.joystick.get_count()):
        myjoy = pygame.joystick.Joystick(i)
        myjoy.init()
        joy.append(myjoy)
        print "Joystick %d: " % (i) + joy[i].get_name()
    print "Depress trigger (button 0) to quit.\n"

    # run joystick listener loop
    joystickControl()

# allow use as a module or standalone script
if __name__ == "__main__":
    main()

