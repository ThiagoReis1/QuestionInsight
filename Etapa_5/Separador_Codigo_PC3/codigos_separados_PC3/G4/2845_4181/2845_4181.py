from numpy import*
COD = array(eval(input("Numeros: ")))

for i in range(size(COD)):
	if(COD[i] == 9):
		COD[i] = COD[i] - 9
	else:	
		COD[i] = COD[i] + 1
print(COD)