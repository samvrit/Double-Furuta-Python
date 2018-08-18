import socket
import time
import serial
from updater import *
import globals
from statemachine import statemachine
from act import act
from shutil import copyfile

# in-line function to obtain the timestamp in milliseconds
millis = lambda: int(round(time.time() * 1000))

# specify the UDP local IP address and port number
UDP_IP = "129.2.182.144"
UDP_PORT = 1100

# configure the UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

# configure the serial COM port
ser = serial.Serial()
ser.baudrate = 2000000
ser.port = 'COM10'
ser.open()

# initialize variables
flag1 = flag2 = flag3 = 0	# flags used to determine reception from each wireless module
curr_state = 'startup'	# initial state of the controller
motor_active = 0	# initial assumption of the motor state
x = [5, 5, 5, 5, 5, 5]	# state vector
flag_graph = 0

t_prev = millis()	# obtain initial timestamp

while True:
	data, addr = sock.recvfrom(1024) # wait for data to be available on the UDP socket
	address = int(addr[0].split('.')[3])	# obtain the last three digits of the remote IP address from the received data packet
	
	data = data.decode("utf-8")	# convert byte array to string
	
	if(ser.in_waiting > 0):	# if bytes are available in the serial input buffer (data from the microcontroller)
		motor_active = int(ser.readline().decode('utf-8'))	# read until a new line character is encountered and convert to int
	
	if(address % 10 == 1):	# if the last digit of the remote IP address is 1, it means that the data is received from wireless module 1
		flag1 = 1	# set flag to 1
		data = data.split(',')	# split the string, since the incoming data contains the angular position and angular velocity, separated by a comma
		if(abs(float(data[1])) < 100):	# a general check to make sure that the incoming data does not contain outliers
			x[0] = float(data[0])	# store the angular position
			x[3] = float(data[1])	# store the angular velocity
	elif(address % 10 == 2):# if the last digit of the remote IP address is 1, it means that the data is received from wireless module 2
		flag2 = 1
		data = data.split(',')
		if(abs(float(data[1])) < 100):
			x[1] = float(data[0])
			x[4] = float(data[1])
	elif(address % 10 == 3):# if the last digit of the remote IP address is 1, it means that the data is received from wireless module 3
		flag3 = 1
		data = data.split(',')
		if(abs(float(data[1])) < 100):
			x[2] = float(data[0])
			x[5] = float(data[1])
	
	if(flag1 == 1 and flag2 == 1 and flag3 == 1):	# only if data is received from all three wireless modules, do the following
		flag1 = flag2 = flag3 = 0	# reset the flags
		t = millis()	# obtain the current timestamp
		dt = t - t_prev	# calculate the difference between the timestamps
		t_prev = t		# current timestamp becomes previous timestamp for the next iteration
		curr_state = statemachine(curr_state,x)	# go through the state machine
		u = act(curr_state,x)	# compute the control signal (torque) based on the system state and state vector
		if(motor_active):	# if motor is active, then start logging the data
			append_file(x,u,curr_state)	# append the states, control signal and system state to file
			flag_graph = 1
		else:
			if(flag_graph):
				flag_graph = 0
				close_file()	# close the current file
				copyfile('states_log.txt','states_log_saved.txt')	# duplicate the current file
				import graphs	# show the graphs
				clear_file()	# clear the current file
		torque = bytes(str(u),'utf-8')+bytes('\n','utf-8')	# format the value to be sent to the microcontroller
		print(dt,x,curr_state,torque)	# show the variables on the console
		ser.write(torque)	# send the torque command to the microcontroller through serial port