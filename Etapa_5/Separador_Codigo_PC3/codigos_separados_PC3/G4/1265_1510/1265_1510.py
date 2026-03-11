#Universidade Federal do Amazonas
#Jorge Trajano da Silva Júnior - 21553770
#Avaliação Parcial 06 - Exercício 2
#01/09/2016
from numpy import *

#solicitação de dados do usuário
p = float(input("Informe o valor de p: "))
x = array(eval(input("Informe o vetor x: ")))
y = array(eval(input("Informe o vetor y: ")))
#variável de auxílio
n = 0
#equação dada pela questão
t = p/(p-1)
xy = (2 * x + 3 * y)
#condição para código
for i in xy:
	n = n + (abs(i))**t #fórmula dentro da raíz
v = n**(1/t) #formula geral
print(round(v,3))