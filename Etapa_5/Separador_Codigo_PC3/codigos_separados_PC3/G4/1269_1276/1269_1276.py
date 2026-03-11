from numpy import*
from math import*
p = float(input("Digite p: "))
x = array(eval(input("Digite o vetor x: ")))
y = array(eval(input("Digite o vetor y: ")))
t = p/(p+1)
xsy = x + y
xmy = x-y
v1 = 0
v2 = 0
for i in range(size(x)):
	v1 = pow(abs(xsy[i]),t) + v1 
	v2 = pow(abs(xmy[i]),t) + v2
v1 = pow(v1,1/t)
v2 = pow(v2,1/t)
v = v1-v2
print(round(v,7))