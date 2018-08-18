f = open("states_log.txt","a+")

def append_file(x,u,state):
	if(state == 'startup'):
		s = 0
	elif(state == 'swing_up'):
		s = 1
	elif(state == 'arm_correction'):
		s = 1.5
	elif(state == 'up_down'):
		s = 2
	elif(state == 'compliant'):
		s = 2.5
	elif(state == 'balance'):
		s = 3
	f.write(str(x[0]) + "," + str(x[1]) + "," + str(x[2]) + "," + str(x[3]) + "," + str(x[4]) + "," + str(x[5]) + "," + str(u) + "," + str(s) + "\n")

def close_file():
	f.close()

def clear_file():
	open("states_log.txt","w").close()