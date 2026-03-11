from numpy import *

vet = array(eval(input()))


r = 0
v =0
i=0

for i in vet:
	if i == 99:
		r = r * 2
	else:
		r = r + i
print(r)
