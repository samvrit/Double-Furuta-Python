# import globals
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import csv

style.use('fivethirtyeight')

x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
tau = []
state = []

with open('up_up.txt','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		x1.append(float(row[0]))
		x2.append(float(row[1]))
		x3.append(float(row[2]))
		x4.append(float(row[3]))
		x5.append(float(row[4]))
		x6.append(float(row[5]))
		tau.append(float(row[6]))
		state.append(float(row[7]))

fig1 = plt.figure()
fig2 = plt.figure()
fig3 = plt.figure()
fig4 = plt.figure()
fig5 = plt.figure()
fig6 = plt.figure()
fig7 = plt.figure()
fig8 = plt.figure()

ax1 = fig1.add_subplot(1,1,1)
ax2 = fig2.add_subplot(1,1,1)
ax3 = fig3.add_subplot(1,1,1)
ax4 = fig4.add_subplot(1,1,1)
ax5 = fig5.add_subplot(1,1,1)
ax6 = fig6.add_subplot(1,1,1)
ax7 = fig7.add_subplot(1,1,1)
ax8 = fig8.add_subplot(1,1,1)

ax1.clear()
ax1.plot(list(range(len(x1))), x1)
ax1.set_ylabel('X1')

ax2.clear()
ax2.plot(list(range(len(x2))), x2)
ax2.set_ylabel('X2')

ax3.clear()
ax3.plot(list(range(len(x3))), x3)
ax3.set_ylabel('X3')

ax4.clear()
ax4.plot(list(range(len(x4))), x4)
ax4.set_ylabel('X4')

ax5.clear()
ax5.plot(list(range(len(x5))), x5)
ax5.set_ylabel('X5')

ax6.clear()
ax6.plot(list(range(len(x6))), x6)
ax6.set_ylabel('X6')

ax7.clear()
ax7.plot(list(range(len(tau))), tau)
ax7.set_ylabel('tau')

ax8.clear()
ax8.plot(list(range(len(state))), state)
ax8.set_ylabel('state')

plt.show()