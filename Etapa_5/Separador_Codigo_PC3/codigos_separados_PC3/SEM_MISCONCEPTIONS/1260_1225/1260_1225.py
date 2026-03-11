from numpy import *
from math import*
p=float(input("um valor real"))
# Leitura do primeiro vetor
x = array(eval(input("Primeiro vetor: ")))
y = array(eval(input("Segundo vetor: ")))
b=0
t = p/p+1
for i in (range(size(x))):
  	b= b + abs(x[i])-(y[i])**t
	r= (b)**(1/t)
print(round(r,4))
