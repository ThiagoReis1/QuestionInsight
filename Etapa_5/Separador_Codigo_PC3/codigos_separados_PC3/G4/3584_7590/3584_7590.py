from numpy import *

v = array(eval(input("")))

i = 0
j = 0


while(i<size(v)):
	if(v[i]>200):
		j = j + v[i] - (v[i]*0.15)
	else:
		j = v[i] + j
	i = i + 1
print(round(j,2))
	