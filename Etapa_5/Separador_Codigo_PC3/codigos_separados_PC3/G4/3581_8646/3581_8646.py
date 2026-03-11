from numpy import *

ver = array(eval(input()))

var = 0
i = 0

while i < size(ver):
	
	if ver[i] >= 40:
		var += ver[i] - 2.5
		
	else:
		var += ver[i]
					  
	i += 1
	
print(round(var, 2))