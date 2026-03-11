from numpy import *
msg = array(eval(input("Digite: ")))
for i in range(size(msg)):
	if 0 < msg[i] <= 9:
		msg[i] = (msg[i]-1)**2
	elif msg[i] == 0:
		msg[i] = (9)**2
print(msg)