from numpy import *

n = array(eval(input("")))
y = 200
i = 0

while(i < size(n)):
	if n[i] == 1:
		y = y/2
	elif n[i] == 2:
		y = y*3
	elif n[i] == 3:
		y = y/2
	elif n[i] == 4:
		y = y* 3
	elif n[i] == 5:
		y = y/2
	elif n[i] == 6:
		y = y*3
	i = i + 1
print(round(y,2))
		