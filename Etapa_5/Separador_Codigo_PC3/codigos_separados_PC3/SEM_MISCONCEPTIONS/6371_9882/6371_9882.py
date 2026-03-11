from numpy import *

vrvl = array(eval(input("insira: ")))
codigo = zeros(size(vrvl), dtype=int)

for i in range(size(vrvl)):
	if vrvl[i] == 0:
		codigo[i] = 9 ** 2
	else:
		codigo[i] = (vrvl[i] - 1) ** 2
	
print(codigo)
