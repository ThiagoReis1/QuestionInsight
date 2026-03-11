from numpy import *
from math import *
vetor = array(eval(input("Digite os valores: ")))
n = size(vetor)
i = 0
soma = 0
while(i<size(vetor)):
	soma = soma + vetor[i]**2
	i = i + 1

media = (soma/n)**(0.5)
print(round(media,2))