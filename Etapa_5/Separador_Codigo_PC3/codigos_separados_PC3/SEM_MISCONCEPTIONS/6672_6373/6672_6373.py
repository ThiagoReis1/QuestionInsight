from numpy import *

vet = eval(input("digite o preco:"))


soma = 0.0
contagem = 0

for precos in vet:
	if precos > 180:
		soma += precos
		contagem +=1
if contagem > 0:
	media = soma / contagem 
else: 
	media = 0.0
print(round(media,2))
		
