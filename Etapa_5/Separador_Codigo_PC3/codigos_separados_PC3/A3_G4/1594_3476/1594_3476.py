from numpy import*
vet=array(eval(input()))
cont = 0
peso = 0
dano = 0
while(cont<size(vet)):
	dano+= vet[cont]*(cont+1)
	cont = cont+1
print(dano)