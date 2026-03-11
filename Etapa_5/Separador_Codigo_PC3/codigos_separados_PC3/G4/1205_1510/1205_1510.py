#Universidade Federal do Amazonas
#Jorge Trajano da Silva Junior - 21553770
#Avaliação Parcial 05 - exercício 01
#18/08/2016
from numpy import *
#solicitação dos valores do usuário
v = array(eval(input("Digite os valores dos saltos: ")))
#variaveis de auxilio
i = 0
j = 0
while(i < size(v)):
	if(v[i] > 8.95):
		j = j + 1
	i = i + 1
print(8.95)
print(j)