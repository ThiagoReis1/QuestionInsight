from numpy import*
from math import*
andar = array(eval(input("andares que parou: ")))

i = 0
soma = 0
e = 0
while (i < size(andar) - 1):
	soma = abs(andar[i + 1] - andar[i])
	e = e + soma
	i = i + 1
print(e)