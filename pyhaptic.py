import serial
import time

class HapticInterface:
    """Creates instances of haptic devices."""
    i = 12345
    def __init__(self, comm_choice):
    	self.ser = ""
    	self.comm_choice = comm_choice
    	self.ascii = True
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
    #def vibrate(self, motor, rhythm, magnitude, duration):
    def vibrate(self):
    	self.ser.write("\x00\x01\n")
    	response = self.ser.read(1)
        if "\00" not in response:
            print "Error"
	def disconnect(self):
		return 'Disconnect Successful'

