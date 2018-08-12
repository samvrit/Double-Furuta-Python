try:
	import cupy as cp
except ModuleNotFoundError:
	import numpy as cp
import math

K_balance = cp.array([0.03, -0.46, -2.57, 0.03, -0.20, -0.25])
K_updown = cp.array([-1.00, 677.15, -0.25, -4.74, 103.49, -0.58])
K_compliant = cp.array([-1.00, 42.29, -30.62, -1.16, 6.56, 1.19])
sw_const = 37
alpha = 0.001
beta = 0.001
TE_ref = 0.1782

def act(curr_state,x):
	x = cp.asarray(x)
	if(curr_state == 'swing_up'):
		if(x[4] is not 0.0):
			u = 0.10
		else:
			TE = 0.1569e0 * math.cos(x[1]) + 0.2126e-1 * math.cos(x[1]) * math.cos(x[2]) - 0.2126e-1 * math.sin(x[1]) * math.sin(x[2]) + (x[4] * ((-0.1e-5 - 0.12e-6 * math.cos(x[2]) ** 2) * math.cos(x[1]) ** 2 + 0.2472e-2 + 0.2e-7 * math.cos(x[2]) ** 2 + (0.1e-5 + 0.4e-7 * math.cos(x[2]) ** 2) * math.cos(x[1]) ** 2 + 0.2e-7 * math.cos(x[1]) ** 2 * math.cos(x[2]) ** 2 + 0.6500e-3 * math.cos(x[2])) / 0.2e1 + x[5] * ((0.2e-7 - 0.6e-7 * math.cos(x[1]) ** 2) * math.cos(x[2]) ** 2 + 0.3250e-3 * math.cos(x[2]) + 0.2344e-3 + 0.2e-7 * math.cos(x[1]) ** 2) / 0.2e1) * x[4] + (x[4] * ((0.2e-7 - 0.6e-7 * math.cos(x[1]) ** 2) * math.cos(x[2]) ** 2 + 0.3250e-3 * math.cos(x[2]) + 0.2344e-3 + 0.2e-7 * math.cos(x[1]) ** 2) / 0.2e1 + x[5] * ((0.2e-7 - 0.2e-7 * math.cos(x[2]) ** 2) * math.cos(x[1]) ** 2 + 0.2344e-3 + 0.2e-7 * math.cos(x[2]) ** 2 + 0.10e-6 * math.cos(x[1]) ** 2 * math.cos(x[2]) ** 2) / 0.2e1) * x[5]
			u = sw_const*(TE_ref - TE)*sign(x[4]*math.cos(x[1]))
	elif(curr_state == 'up_down'):
		u = -cp.dot(K_updown,x)
	elif(curr_state == 'balance'):
		u = -cp.dot(K_balance,x)
	elif(curr_state == 'arm_correction'):
		u = alpha*x[0] - beta*x[3]
	elif(curr_state == 'compliant'):
		u = -cp.dot(K_compliant,x)
	return round(float(u),4)

def sign(a):
	if(a < 0):
		return -1
	elif(a > 0):
		return 1
	else:
		return 0