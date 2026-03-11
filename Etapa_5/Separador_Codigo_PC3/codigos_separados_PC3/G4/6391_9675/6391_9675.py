from numpy import *

cod = array(eval(input()))
#se n=7 for a entrada, (n-1)**3
#se (6)**3 = 216
for i in range(size(cod)):
	if cod[i] == 0:
		cod[i] = 9**3
	else:
		cod[i] = (cod[i]-1)**3
print(cod)