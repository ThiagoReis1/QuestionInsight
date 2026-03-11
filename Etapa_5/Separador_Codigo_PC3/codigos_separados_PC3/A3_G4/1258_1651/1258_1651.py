from numpy import *
from math import *

p=float(input("Qual eh o numero real?"))
x = array(eval(input("Qual eh o vetor?")))
y = array(eval(input("Qual eh o vetor?")))
h=0
n=0
j=0
t = ((p)/(p+1))
xy=(x+y)
for i in xy:
	n=n+(abs(i))**t
v= n**(1/t)
print(round(v,3))
