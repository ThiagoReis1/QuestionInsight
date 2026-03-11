#Universidade Federal do Amazonas
#Jorge Trajano da Silva Junior - 21553770
#Avaliação Parcial 05 - exercício 02
#18/08/2016
from numpy import *
#solicitação das temperaturas do usuário
v = array(eval(input("Informe as temperaturas do Rio Solimoes: ")))
#variaveis de auxilio
i = 0 
j = 0
t = size(v)
while(i < size(v)): #controle de valores inválidos
	if(v[i] > 40):
		j = j + 1
	i = i + 1
t = size(v) - j #tamanho do vetor sem os valores invalidos
v2 = array(ones(t,dtype=float))
i = 0
k = 0
while(i < size(v)):
	if(v[i] < 40):
		v2[k] = v[i] #substituição dos valores do vetor resultante
		k = k + 1
	i = i + 1
print(v2)