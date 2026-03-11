#Universidade Federal do Amazonas
#Aluna: Ingrid de Lira Lima
#Exercicio: 02 

from math import*
from numpy import* 

p= float(input("digite:"))
x= array(eval(input("digite o valor de x: ")))
y= array(eval(input("digite o valor de y: ")))

t= p/(p+1)
F=0
for i in range (size(x)):
	F+=abs(2*x[i]+3*y[i])**t
Resultado= F**(1/t)
print(round(Resultado,7))






