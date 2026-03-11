from numpy import *

ver = array(eval(input()))

op_1 = size(ver)
op_2 = zeros(op_1, dtype=int)

for i in range(size(ver)):
	
	if ver[i] == 9:
		op_2[i] = 0
	
	else:
		op_2[i] = (ver[i] + 1) ** 2
	
print(op_2)