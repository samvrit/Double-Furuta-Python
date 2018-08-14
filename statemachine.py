import math

def statemachine(curr_state, x):
	next_state = curr_state
	if(curr_state == 'startup'):
		cond1 = (abs(x[1]) > deg2rad(20))
		cond2 = (abs(x[1]) <= deg2rad(20))
		cond3 = (abs(x[1]) <= deg2rad(15)) and (abs(x[2]) <= deg2rad(10))
		if(cond1):
			next_state = 'swing_up'
		elif(cond2):
			next_state = 'up_down'
		elif(cond3):
			next_state = 'balance'
	elif(curr_state == 'swing_up'):
		cond1 = (abs(x[1]) <= deg2rad(20))
		cond2 = (abs(x[1]) >= deg2rad(89)) and (abs(x[1]) <= deg2rad(91))
		cond3 = (abs(x[1]) <= deg2rad(15)) and (abs(x[2]) <= deg2rad(10))
		if(cond1):
			next_state = 'up_down'
		elif(cond2):
			next_state = 'arm_correction'
		elif(cond3):
			next_state = 'balance'
	elif(curr_state == 'up_down'):
		cond1 = (abs(x[2]) <= deg2rad(10)) and (abs(x[4]) <= 2) and (abs(x[5]) <= 7)
		cond2 = (abs(x[1]) > deg2rad(20))
		cond3 = (abs(x[1]) <= 0.1) and (abs(x[4]) <= 0.4) and (abs(x[2]) >= deg2rad(170)) and (abs(x[5]) <= 10)
		if(cond1):
			next_state = 'balance'
		elif(cond2):
			next_state = 'swing_up'
		elif(cond3):
			next_state = 'compliant'
	elif(curr_state == 'balance'):
		cond1 = (abs(x[1]) > deg2rad(60))
		cond2 = (abs(x[1]) <= deg2rad(1)) and (abs(x[2]) <= deg2rad(1)) and (abs(x[3]) <= deg2rad(1))
		cond3 = abs(x[1]) < deg2rad(20) and abs(x[2]) > deg2rad(60)
		if(cond1):
			next_state = 'swing_up'
		elif(cond3):
			next_state = 'up_down'
	elif(curr_state == 'arm_correction'):
		cond1 = (abs(x[1]) <= deg2rad(15)) and (abs(x[2]) <= deg2rad(10))
		cond2 = (abs(x[1]) < deg2rad(60)) or (abs(x[1]) > deg2rad(120))
		if(cond1):
			next_state = 'balance'
		elif(cond2):
			next_state = 'swing_up'
	elif(curr_state == 'compliant'):
		cond1 = (abs(x[1]) > deg2rad(35)) or (abs(x[4]) > 20)
		if(cond1):
			next_state = 'up_down'
	return next_state

def deg2rad(a):
	return a*math.pi/180