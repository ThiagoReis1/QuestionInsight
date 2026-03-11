from numpy import *

n = array(eval(input()))
x = zeros(size(n),dtype = int)
for i in range(size(n)):
	if n[i] == 0:
		x[i] = n[i] + 1
	elif n[i] == 1:
		x[i] = n[i] + 1
	elif n[i] == 2:
		x[i] = n[i] + 1
	elif n[i] == 3:
		x[i] = n[i] + 1
	elif n[i] == 4:
		x[i] = n[i] + 1
	elif n[i] == 5:
		x[i] = n[i] + 1
	elif n[i] == 6:
		x[i] = n[i] + 1
	elif n[i] == 7:
		x[i] = n[i] + 1
	elif n[i] == 8:
		x[i] = n[i] + 1
	elif n[i] == 9:
		x[i] = 0
print(x)