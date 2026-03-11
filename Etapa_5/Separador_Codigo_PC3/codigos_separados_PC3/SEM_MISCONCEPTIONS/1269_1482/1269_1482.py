#Thaynara Marques - 21552463
from numpy import*
from math import*

p = float(input())
x = array(eval(input()))
y = array(eval(input()))
t = p / (p+1)
q=0
for i in range(size(x)):
	q = (((abs(x[i]+y[i]) - (abs(x[i]-y[i]))**t) + q
q = q**(1/t)
print(round(q,7))