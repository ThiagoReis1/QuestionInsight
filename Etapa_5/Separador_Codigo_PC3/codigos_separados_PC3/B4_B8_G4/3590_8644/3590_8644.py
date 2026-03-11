from numpy import *

v = array(eval(input("")))
c = 0
for i in range(size(v)):
	if(v[i] == 1):
		c += 10
	elif(v[i] == 2):
		c += 5
	elif(v[i] == 3):
		c += 0
	elif(v[i] == 4):
		c += 5
	elif(v[i] == 5):
		c += 20
	elif(v[i] == 6):
		c += 10
print(sum(c))