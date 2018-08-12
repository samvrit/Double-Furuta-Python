import globals
f = open("states_log.txt","a+")

def update_globals(x,u):
	f.write(str(x[0]) + "," + str(x[1]) + "," + str(x[2]) + "," + str(x[3]) + "," + str(x[4]) + "," + str(x[5]) + "," + str(u) + "\n")
	
	