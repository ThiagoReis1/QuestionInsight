from numpy import *

n = array(eval(input("Vetor: ")))

for i in n:
	if i > 180:
		i = i + i
		
	else:
		print("0.0")