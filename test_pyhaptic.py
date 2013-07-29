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
    print "Query All"
    two_d_display.qry_all()
    print "Setting Binary"
    two_d_display.set_binary()
    print "Vibrating Motor A"
    two_d_display.vibrate()