from numpy import *

vetor = array(eval(input("notas: ")))
peso = array([3,2,4,1,3])
tamanho = size(peso)-1

i = 0
soma = 0
while i <= tamanho:
	s = vetor[i] * peso[i]
	soma = soma + s
	i +=1
print(round(soma/sum(peso),2))