from numpy import *

cod = array(eval(input()),dtype=int)

for i in range(size(cod)):
	if cod[i] == 9:
		cod[i] = 0
	else:
		cod[i] = (cod[i] + 1) ** 2
print(cod)