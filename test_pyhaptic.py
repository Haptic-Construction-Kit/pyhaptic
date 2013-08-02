import os
import glob
import sys
import time
import serial
import logging
import random

logging.basicConfig(level=logging.DEBUG)

from pyhaptic import HapticInterface

def find_comm_port():
    comm_port = []
    if os.name == 'posix':
        comm_port = glob.glob('/dev/tty.*')
        comm_port.extend( glob.glob('/dev/ttyACM*'))
        comm_port.extend( glob.glob('/dev/ttyUSB*'))
    elif os.name == 'nt':
        available = []
        for i in range(256):
            try:
                s = serial.Serial(i)
                available.append('COM'+str(i + 1))
                s.close()
            except serial.SerialException:
                pass
        comm_port.extend(available)
    print "Printing current available comm ports.\n"
    for i in comm_port:
        print i
    comm_choice = raw_input("\nPlease choose the full path to the comm port that the haptic controller is connected to:") 
    return comm_choice

def function_zero():
    print "running zero"
    for x in xrange(two_d_display.qry_number_motors()):
        two_d_display.vibrate(x,0,0,1)
        time.sleep(.1)
    print "completed zero"

def function_one():
    print "running one"
    number = two_d_display.qry_number_motors()
    for x in xrange(number):
        two_d_display.vibrate(x,0,0,1)
        time.sleep(.1)
    for x in xrange(number,0,-1)):
        two_d_display.vibrate(x,0,0,1)
        time.sleep(.1)
    print "completed one"

def function_two():
    print "running two"
    num_motors = two_d_display.qry_number_motors()
    for x in xrange(num_motors):
        if x % 8 == 0:
            two_d_display.vibrate(x,0,0,1)
    time.sleep(.5)
    for x in xrange(num_motors):
        if x % 8 == 1:
            two_d_display.vibrate(x,0,0,1)
    time.sleep(.5)
    for x in xrange(num_motors):
        if x % 8 == 2:
            two_d_display.vibrate(x,0,0,1)
    time.sleep(.5)
    for x in xrange(num_motors):
        if x % 8 == 3:
            two_d_display.vibrate(x,0,0,1)
    time.sleep(.5)
    for x in xrange(num_motors):
        if x % 8 == 4:
            two_d_display.vibrate(x,0,0,1)
    time.sleep(.5)
    for x in xrange(num_motors):
        if x % 8 == 5:
            two_d_display.vibrate(x,0,0,1)
    time.sleep(.5)
    for x in xrange(num_motors):
        if x % 8 == 6:
            two_d_display.vibrate(x,0,0,1)
    time.sleep(.5)
    for x in xrange(num_motors):
        if x % 8 == 7:
            two_d_display.vibrate(x,0,0,1)
    time.sleep(1)
    # And back the other direction.
    for x in xrange(num_motors):
        if x % 8 == 6:
            two_d_display.vibrate(x,0,0,1)
    time.sleep(.5)
    for x in xrange(num_motors):
        if x % 8 == 5:
            two_d_display.vibrate(x,0,0,1)
    time.sleep(.5)
    for x in xrange(num_motors):
        if x % 8 == 4:
            two_d_display.vibrate(x,0,0,1)
    time.sleep(.5)
    for x in xrange(num_motors):
        if x % 8 == 3:
            two_d_display.vibrate(x,0,0,1)
    time.sleep(.5)
    for x in xrange(num_motors):
        if x % 8 == 2:
            two_d_display.vibrate(x,0,0,1)
    time.sleep(.5)
    for x in xrange(num_motors):
        if x % 8 == 1:
            two_d_display.vibrate(x,0,0,1)
    time.sleep(.5)
    for x in xrange(num_motors):
        if x % 8 == 0:
            two_d_display.vibrate(x,0,0,1)
    print "completed two"

def function_three():
    print "running three"
    num_motors = two_d_display.qry_number_motors()
    for x in xrange(num_motors):
        two_d_display.vibrate(random.randrange(num_motors),0,0,1)
        time.sleep(.1)
    print "completed three"

def function_four():
    print "running four"
    print "completed four"

def function_five():
    print "running five"
    print "completed five"

def function_six():
    print "running six"
    print "completed six"

def function_seven():
    print "running seven"
    print "completed seven"

def function_eight():
    print "running eight"
    print "completed eight"

def function_nine():
    print "running nine"
    print "completed nine"

if __name__ == '__main__':
    
    two_d_display = HapticInterface(find_comm_port())
    try:
        two_d_display.connect()
    except:
        print "Failed to connect on ..."
        sys.exit(1)
    
    print "enter a number 0-9 to activate that function"
    print "anything else to exit"
    while True:
        comm_choice = sys.stdin.read(1)
        sys.stdin.read(1) #dump the newline char
        if comm_choice == "0":
            function_zero()
        elif comm_choice == "1":
            function_one()
        elif comm_choice == "2":
            function_two()
        elif comm_choice == "3":
            function_three()
        elif comm_choice == "4":
            function_four()
        elif comm_choice == "5":
            function_five()
        elif comm_choice == "6":
            function_six()
        elif comm_choice == "7":
            function_seven()
        elif comm_choice == "8":
            function_eight()
        elif comm_choice == "9":
            function_nine()
        else:
            sys.exit(0)
