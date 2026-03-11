from numpy import *

vet = array(eval(input("insira o vetor: ")))

a = vet[0]
b = vet[1]

c = 5
d = 1

numerador = (a * c) + (b * d)
denominador = c + d

media = numerador / denominador

print(round(media, 2))
	