from numpy import *
pesos = [2,1,5]
vet = array (eval(input()))
if size(vet)== size(pesos):
	media=0
	p=0
	i=0
	while i < size(vet):
		media = media +(vet[i]*pesos[i])
		p=p+pesos[i]
		i=i+1
print(round(media/p,2))