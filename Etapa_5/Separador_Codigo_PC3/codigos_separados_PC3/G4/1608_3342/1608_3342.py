from numpy import *

p = array(eval(input(": ")))

i=0
t=0
while i < size(p):
	t=t+p[i]
	if t > 75:
		t=75
	i+=1	
print(t)
