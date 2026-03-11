from numpy import *
total = 0
k = 0
ent = array(eval(input()))
for i in ent:
	total += i*0.15
	k +=1
print(round(total,2))