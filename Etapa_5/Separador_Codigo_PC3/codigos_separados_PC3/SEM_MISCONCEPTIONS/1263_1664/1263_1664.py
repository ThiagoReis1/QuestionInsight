#---------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS	
# LARISSA SANTOS BRITO - 21454598
# DATA: 25/08/2016
# AVALIAÇÃO 06 - EXERCÍCIO 01
# OBJETIVO: Fazer a leitura de um número real e dois vetores
#---------------------------------
from numpy import *

num = array(eval(input("digite um numero:")))
vetor1 = array(eval(input("primeiro vetor:")))
vetor2 = array(eval(input("segundo vetor:")))

q = num / (num +1)

for i in range(0, size(vetor1)):
	vetor1[i] = abs(i) ** q
	soma1 = sum(vetor1)
for i in range(0, size(vetor2)):
	vetor2[i] = abs(i) ** q
	soma2 = sum(vetor2)
norma1 = 1 / soma1 ** q
norma2 = 1 / soma2 ** q 

num1 = 2 * norma1
num2 = 3 * norma2
total = round(num1 + num2, 7)

print (total)

					