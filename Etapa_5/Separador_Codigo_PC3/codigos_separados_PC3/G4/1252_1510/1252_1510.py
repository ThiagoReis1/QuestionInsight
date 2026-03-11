#Universidade Federal do Amazonas
#Jorge Trajano da Silva Júnior - 21553770
#Avaliação Parcial 06 - Exercício 1
#01/09/2016
from numpy import *
#Solicitar valores do usuário
v = array(eval(input("Informe os valores de v: ")))
#Dados informados da questão
A = min(v)
B = max(v)
C = 0.6 * A + 0.4 * B
D = 0.3 * A + 0.7 * B
#Criação do vetor x
x = array(zeros(2, dtype=int))
m = 0
n = 0
#leitura do código
for i in range(size(v)):
	if(v[i] >= A and v[i] < C):
		m = m + 1
		x[0] = m
	if(v[i] >= C and v[i] < D):
		n = n + 1
		x[1] = n

print(x)
		