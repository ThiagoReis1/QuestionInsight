from numpy import *

x = array(eval(input("vetor: ")))
i = 0
if (x[i] > 80):
	x[i] = x[i] - 5
	total = sum(x) - 5
	i = i + 1

else:
	total = sum(x) 
	
print(round(total,2))








