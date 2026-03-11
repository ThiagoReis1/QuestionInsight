#Karoline Oliveira da Costa
#25 de Agosto de 2016
#AV.06 Questão 2
from numpy import*
from math import*

p=float(input("Digite um numero p: "))
x=array(eval(input("Digite o vetor x: ")))
y=array(eval(input("Digite o vetor y: ")))
z= 2 * x - y
p=p>1
t= p / p-1
for i in range(size(z)):
	z[i]= (2 * x[i])- y[i]
	norma = sqrt(abs(z[i])** 1/t)
print(round(norma,4))