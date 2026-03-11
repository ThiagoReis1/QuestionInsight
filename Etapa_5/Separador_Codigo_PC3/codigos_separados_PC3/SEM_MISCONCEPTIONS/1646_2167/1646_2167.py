from numpy import *
indice = array(eval(input("Digite os valores: ")))
acum = 0

for i in range(size(indice)):
	if(indice[i] <= 50):
		acum = acum + 1
print(acum)		
vcont = zeros(acum, dtype=int)
cont = 0
for j in range(size(indice)):
	if(indice[j] <= 50):
		vcont[cont] = j
		cont = cont + 1
print(vcont)
