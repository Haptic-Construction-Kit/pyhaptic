import serial
import time
import struct

class HapticInterface:
    """Creates instances of haptic devices."""
    i = 12345
    def __init__(self, comm_choice):
    	self.ser = ""
    	self.comm_choice = comm_choice
    	self.ascii = True
    def __build_binary(self, motor, rhythm, magnitude, duration):
        #Commands are 16 bits each, big endian
        #ttttmmmmRRRMMddd
        vibrate_type = 0
        motor_mask = 15
        rhythm_mask = 7
        magnitude_mask = 3
        duration_mask = 7
        
        byte1 = vibrate_type << 4 | (motor & motor_mask)
        byte2 = (rhythm & rhythm_mask) << 5 | (magnitude & magnitude_mask) << 3 | (duration & duration_mask)
        result = struct.pack('>BB', byte1, byte2)
        print "built command string:" + result
        return result
    def set_ascii(self):
    	#self.__send('\b0011000000000000')
    	self.__send('\b0000000000001100')
    def set_binary(self):
    	self.__send("BGN\n")
    def __send(self, command):
    	self.ser.write(command)
        response = self.ser.readlines()
        if not any("STS 0" in s for s in response):
    	    print "Error"
    def connect(self):
        self.ser = serial.Serial(self.comm_choice, timeout=1)
        print "Connecting!"
    def qry_all(self):
    	self.__send("QRY ALL\n")
    def qry_motors(self):
    	return 'Motors Queried'
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
        for x in response:
            print ord(x)
        if "\00" not in response:
            print "Error"
	def disconnect(self):
		return 'Disconnect Successful'

