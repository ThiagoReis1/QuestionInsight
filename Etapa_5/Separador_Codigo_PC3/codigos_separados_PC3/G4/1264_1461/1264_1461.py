# Monalisa Pereira 21600560
# 250816
# Av 06 - Ex 02

from numpy import *

p = eval(input("Insira um número real >1: "))
x = array(eval(input("Insira o vetor x: ")))
y = array(eval(input("Insira o vetor y: ")))

t = p/(p+1)
j = 0
q = 0
i = 0

while (i<size(x)):
	x[i] = x[i]-2*y[i]
	i = i+1
	
while (j<size(x)):
	q = q+(abs(x[j])**t)
	j = j+1

qxy = q**(1/t)

print(round(qxy,8))