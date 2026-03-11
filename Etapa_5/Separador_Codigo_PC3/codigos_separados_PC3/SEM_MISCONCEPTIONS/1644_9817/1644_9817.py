from numpy import *
nfinais= array(eval(input("Insira as notas:")))
cont= 0

for i in range(size(nfinais)):
	if nfinais[i] < 5:
		cont= cont + 1
		print(cont)
	
reprovados= zeros(cont, dtype=int)
ind= 0

for i in range(size(reprovados)):
	if nfinais[i] < 5:
		reprovados[i]= reprovados[i] + 1
		ind= ind + 1
		
print(reprovados)



	