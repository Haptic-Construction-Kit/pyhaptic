import os
import glob
import sys

from pyhaptic import HapticInterface

def find_comm_port():
    if os.name == 'posix':
    	comm_port = glob.glob('/dev/tty.*')
    	print "Printing current available comm ports.\n"
    	for i in comm_port:
        	print i
    	comm_choice = raw_input("\nPlease choose the full path to the comm port that the haptic controller is connected to:") 
    return comm_choice
def function_zero():
    print "running zero"
    two_d_display.vibrate(0,0,0,1)
    two_d_display.vibrate(1,0,0,1)
    two_d_display.vibrate(2,0,0,1)
    two_d_display.vibrate(3,0,0,1)

    print "completed zero"

def function_one():
    print "running one"
    print "completed one"

def function_two():
    print "running two"
    print "completed two"

def function_three():
    print "running three"
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
