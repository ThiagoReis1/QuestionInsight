from numpy import *
notas = array(eval(input("notas: ")))
i = 0
soma = 0
peso = 0
while(i < size(notas)):
	soma = soma + notas[i] * (i + 1)
	peso = peso + (i + 1)
	i = i + 1
media = soma / peso
print(round(media, 2))