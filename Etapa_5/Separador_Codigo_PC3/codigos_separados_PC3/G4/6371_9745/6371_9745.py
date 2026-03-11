from numpy import*

ent = array(eval(input("vetor: ")))

aux = zeros(size(ent), dtype=int)

for i in range(size(ent)):
	if ent[i] == 0:
		aux[i]= 81
	else:
		aux[i]= (ent[i] - 1) ** 2
	
print(aux)