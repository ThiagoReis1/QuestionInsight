from numpy import *

vetor_custo = array(eval(input("Custo de cada item: ")))

i = 0
j = 0

while i < size(vetor_custo):
	if vetor_custo[i] > 160:
		j += 1
	else:
		pass
	i += 1
	
print(round(sum(vetor_custo) - 25*j, 2))