import os
import glob

from pyhaptic import HapticInterface

def find_comm_port():
    if os.name == 'posix':
    	comm_port = glob.glob('/dev/tty.*')
    	print "Printing current available comm ports.\n"
    	for i in comm_port:
        	print i
    	comm_choice = raw_input("\nPlease choose the full path to the comm port that the haptic controller is connected to:") 
    return comm_choice

if __name__ == '__main__':
    
    two_d_display = HapticInterface(find_comm_port())
    try:
    	two_d_display.connect()
    except:
        print "Failed to connect on ..."
    print "Vibrating Motors"
    two_d_display.vibrate(0,0,0,1)
    two_d_display.vibrate(1,0,0,1)
    two_d_display.vibrate(2,0,0,1)
    two_d_display.vibrate(3,0,0,1)