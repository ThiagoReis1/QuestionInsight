from numpy import *
i =0
total = 0

v = array(eval(input()))

while(i<size(v)):
	if(v[i]>=80):
		total += v[i] -5
	else:
		total += v[i]
	i +=1

print(round(total,2))
	