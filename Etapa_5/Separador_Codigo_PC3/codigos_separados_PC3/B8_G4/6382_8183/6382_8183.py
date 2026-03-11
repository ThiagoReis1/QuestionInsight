from numpy import *

n = array(eval(input(" ")))

for i in range(size(n)):
	if (n[i] == 9):
		n[i] = 0
		
	elif(n[i] != 9):
		n[i] = (n[i] + 1)**2
print(n)
		

	