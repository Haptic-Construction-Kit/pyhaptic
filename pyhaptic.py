"""
.. module:: HapticInterface 
   :platform: Linux, Windows, Mac
   :synopsis: Part of the Haptic Construction Kit https://github.com/Haptic-Construction-Kit/ 

.. moduleauthor:: see contributors.md


"""

import serial
import time
import struct
import logging

class HapticInterface:
    """Creates instances of haptic devices."""
    VERSION = 1
    def __init__(self, comm_choice):
    	self.ser = ""
    	self.comm_choice = comm_choice
    	self.ascii = True
    def __build_binary(self, motor, rhythm, magnitude, duration):
        #Commands are 16 bits each, big endian
        #ttmmmmmmRRRMMddd
        vibrate_type = 0
        motor_mask = 63
        rhythm_mask = 7
        magnitude_mask = 3
        duration_mask = 7
        
        byte1 = vibrate_type << 6 | (motor & motor_mask)
        byte2 = (rhythm & rhythm_mask) << 5 | (magnitude & magnitude_mask) << 3 | (duration & duration_mask)
        result = struct.pack('>BB', byte1, byte2)
        logging.debug('built command string: ' + result)
        return result
    def set_ascii(self):
        self.ser.write("\xC0\x00")
        response = self.ser.read(1)
        if "\00" not in response:
            for x in response:
                logging.debug('Error Switching to ascii' + str(x))
        else:
            self.ascii = True
    def set_binary(self):
    	self.__send("BGN\n")
        #assume success until we get the exceptions implemented
        self.ascii = False
    def __send(self, command):
    	self.ser.write(command)
        response = self.ser.readlines()
        if not any("STS 0" in s for s in response):
    	    logging.debug('Error sending ascii command: ' + command)
        return response
    def connect(self):
        """Attempts a connection over serial to the haptic device.

        Args:
        none.

        Returns:
        none.

        Raises:
        SerialException

        """
	self.ser = serial.Serial(self.comm_choice, timeout=.1)
        #check that meets min version
    def qry_ver(self):
        """Query version number of controller firmware.

        Args:
            none.

        Returns:
            int.  The version number of controller firmware:

        """
	if not (self.ascii): #we need to be in ascii
            self.set_ascii()
        self.ser.write("QRY VER\n")
        response = self.ser.readline()
        response_list = response.split(" ")
        ver = 0
	if ((len(response_list) == 3) & (response_list[0] == "RSP")):
            ver = int(response_list[2])
        else:
            #throw communication exception?
            pass
        logging.debug( 'Version Queried:' + str(ver) )
	return ver
    def qry_number_motors(self):
        """Query number of motors present.
        
        Args:
            none.
        
        Returns:
            int.  The number of motors present:

        """
        if not (self.ascii): #we need to be in ascii
            self.set_ascii()
        self.ser.write("QRY MTR\n")
        response = self.ser.readline()
        response_list = response.split(" ")
        if ((len(response_list) == 3) & (response_list[0] == "RSP")):
            motors = int(response_list[2])
        else:
            motors = 0
        logging.debug('Motors Queried: ' + str(motors))
        return motors
    def qry_magnitudes(self):
    	pass
    def qry_rhythms(self):
    	pass
    def learn_rhythm(self):
    	return 'Rhythm Learned'
    def learn_magnitude(self):
    	pass
    def vibrate(self, motor, rhythm, magnitude, cycles):
        """Vibrate a motor.

        Args:
         |  motor(int): Motor to select. 0 indexed.
         |  rhythm(int): Stored rhythm to select. 0 indexed. Use qry_rhythms to see available and learn_rhythm to store rhythms.
         |  magnitude(int): Stored magnitude to select. 0 indexed. Use qry_magnitudes to see available and learn_magnitude to store magnitudes.
         |  cycles(int): Number of times to run stored magnitude. 0-7 are valid. 7 is continuous. 0 is used to interrupt a vibration and disable motor.

        Returns:
	    none.

        """
        if(self.ascii):
            self.set_binary()
        self.ser.write(self.__build_binary(motor, rhythm, magnitude, cycles))
        response = self.ser.read(1)
        if "\00" not in response:
            for x in response:
                logging.debug( 'Error Vibrating' + str(x) )
	def disconnect(self):
		return 'Disconnect Successful'

