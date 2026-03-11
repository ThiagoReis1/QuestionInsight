from numpy import *

x = array(eval(input("Digite: ")))

for i in range(size(x)):
	if x[i] == 0:
		x[i] = 9**3
	else:
		x[i] = (x[i] - 1)**3
	
print(x)