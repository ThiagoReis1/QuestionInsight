from numpy import*
from numpy.linalg import*

custo = array(eval(input("insira o vetor de custos: ")))
total = 0
#a = shape(custo)[0]

for j in range(shape(custo)[0]):
	if((custo[j])>80):
		total = total + custo[j] - (custo[j]*15/100)
	else:
		total = total + custo[j]
print(round(total,2))