from numpy import *

vc = array(eval(input()))
i = 0

while(i < size(vc)):
	
	if(vc[i] > 80):
		
		vc[i] = vc[i] - (vc[i] * (15/100))
	
	i = i + 1
	
t = sum(vc)

print(round(t, 2))