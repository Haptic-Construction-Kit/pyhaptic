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
        self.ser = serial.Serial(self.comm_choice, timeout=.1)
        #check that meets min version
    def qry_ver(self):
        self.__send("QRY VER\n")
        response = self.ser.readline()
        response_list = response.split(" ")
        if ((len(response_list) == 3) & (response_list[0] == "RSP")):
            ver = int(response_list[2])
        else:
            #throw communication exception?
            pass
        logging.debug( 'Version Queried:' + str(ver) )
        return ver
    def qry_all(self):
    	self.__send("QRY ALL\n")
    def qry_number_motors(self):
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
    def vibrate(self, motor, rhythm, magnitude, duration):
        if(self.ascii):
            self.set_binary()
        self.ser.write(self.__build_binary(motor, rhythm, magnitude, duration))
        response = self.ser.read(1)
        if "\00" not in response:
            for x in response:
                logging.debug( 'Error Vibrating' + str(x) )
	def disconnect(self):
		return 'Disconnect Successful'

