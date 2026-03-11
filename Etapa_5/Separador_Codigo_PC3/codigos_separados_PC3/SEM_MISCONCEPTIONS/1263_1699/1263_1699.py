#---------------------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS
# ANA REBECA CAVALCANTE EVANGELISTA 
# MATRICULA: 21456290
# DATA: 25/08/2016
# AVALIAÇÃO PARCIAL 06
#---------------------------------------------------------

from numpy import *

num = array(eval(input("Digite um numero: ")))
vetor1 = array(eval(input("Digite os valores do primeiro vetor: ")))
vetor2 = array(eval(input("Digite os valores do segundo vetor: ")))

q = num / (num + 1)

num1 = 2 * vetor1
num2 = 3 * vetor2
soma[i] = num1 + num2

for i in range(0, size(soma)):
	soma[i] = abs(i) ** q
	total = sum(soma)

norma = 1 / total ** q


print(round(norma, 7))
	
		
