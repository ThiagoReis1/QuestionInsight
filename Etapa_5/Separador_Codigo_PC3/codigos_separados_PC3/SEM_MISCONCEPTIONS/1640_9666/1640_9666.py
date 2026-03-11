from numpy import *

entrada = eval(input())
qtd_impars = 0
id_impars = []

for i in range(len(entrada)):
	if entrada[i] % 2 != 0:
		qtd_impars += 1
		id_impars.append(i)
		
print(qtd_impars)
print(array(id_impars))