from numpy import *

ver = array(eval(input()))
cont_1 = 0
cont_2 = 0

for i in range(size(ver)):
	if ver[i] > 20:
		cont_1 += ver[i]
		cont_2 += 1
		
if cont_2 != 0:
	op = cont_1 / cont_2

else:
	op = 0

print(round(op, 2))

