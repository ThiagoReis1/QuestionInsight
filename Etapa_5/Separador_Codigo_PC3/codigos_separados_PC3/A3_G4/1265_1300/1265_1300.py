from numpy import*
from math import*
p = eval(input("digite um numero :"))
x = array(eval(input("digite um numero : ")))
y = array(eval(input("digite um numero : ")))
t= p / (p-1)
v=2*x+3*y
s = 0
sj = 0
for i in v:
	s=s+(abs(i))**t
xx = (s)**(1/t)
print(round(xx,3))