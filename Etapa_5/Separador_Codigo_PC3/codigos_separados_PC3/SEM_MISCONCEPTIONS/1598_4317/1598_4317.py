from numpy import *

v = array(eval(input("Informe o vetor: ")))

descontos = 0
i = 0

while (i < size(v)):
	if v[i] > 90:
		descontos = descontos + 6.5
	i = i + 1
print(round(sum(v) - descontos,2))
