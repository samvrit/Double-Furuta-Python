import socket
import time
import serial
import cupy as cp
from statemachine import statemachine
from act import act

micros = lambda: int(round(time.time() * 1000000))

UDP_IP = "129.2.182.144"
UDP_PORT = 1100

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

ser = serial.Serial()
ser.baudrate = 2000000
ser.port = 'COM10'

flag1 = flag2 = flag3 = 0

curr_state = 'startup'
x = [5, 5, 5, 5, 5, 5]

t_prev = micros()

while True:
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	address = int(addr[0].split('.')[3])
	
	data = data.decode("utf-8")
	
	if(address % 10 == 1):
		flag1 = 1
		data = data.split(',')
		x[0] = float(data[0])
		x[3] = float(data[1])
	elif(address % 10 == 2):
		flag2 = 1
		data = data.split(',')
		x[1] = float(data[0])
		x[4] = float(data[1])
	elif(address % 10 == 3):
		flag3 = 1
		data = data.split(',')
		x[2] = float(data[0])
		x[5] = float(data[1])
	
	if(flag1 == 1 and flag2 == 1 and flag3 == 1):
		flag1 = flag2 = flag3 = 0
		t = micros()
		dt = t - t_prev
		t_prev = t
		curr_state = statemachine(curr_state,x)
		u = act(curr_state,x)
		print(dt,x,curr_state)
		torque = bytes(str(u),'utf-8')