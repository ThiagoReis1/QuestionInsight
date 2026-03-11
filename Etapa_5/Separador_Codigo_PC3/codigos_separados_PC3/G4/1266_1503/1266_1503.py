from numpy import*
from math import*

p =  float(input("Digite P: "))
x = array(eval(input(" Digite seu vetor X: ")))
y = array(eval(input(" Digite seu vetor Y: ")))

t = p/(p-1)
v = 0
for i in range(size(x)):
	v = (x[i]*2-y[i])**t + v
d = abs(v)**1/t
print(round(d, 4))

