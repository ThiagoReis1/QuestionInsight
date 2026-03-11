#Universidade Federal do Amazonas
#Thiago Tuma Camilo 21600549
from numpy import *
p = float(input("Digite um número:"))
x = array(eval(input("Digite o valor do vetor x:")))
y = array(eval(input("Digite o valor do vetor y:")))
t = p/(p+1)
norma = 0
for i in range(size(x)):
	norma = (abs(x[i] - y[i]) ** t) + norma
norma = norma ** (1/t)
print(round(norma, 4))