from numpy import*
from math import*
p=float(input("digite um valor:"))
x=array(eval(input("Informe o vetor 1:")))
y=array(eval(input("Informe o vetor 2:")))
b=0
t=p/p+1
for i in range(size(x)):
	b=b+abs(sqrt(x[i]+y[i])**t)
r=(b)**(1/t)
print(round(r,3))