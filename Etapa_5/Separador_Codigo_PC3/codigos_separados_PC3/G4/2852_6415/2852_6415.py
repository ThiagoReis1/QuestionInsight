from numpy import*

vet = array(eval(input("Digite o numeros:")), dtype=int)
j = 0
resu = 0

for j in range(size(vet)):
	if(vet[j] != 88):
		resu = resu + vet[j]
	else:
		resu = resu / 2

print(resu)



