from numpy import *
from math import *
p = float(input("Digite um numero real maior que um: "))
x = array(eval(input("informe um vetor: ")))
y = array(eval(input("informe um vetor: ")))
t = p / (p+1)
for i in range(0,size(x)):
	a = (abs((x[i] + y[i])) ** t) ** (1/t)
	b = (abs((x[i] - y[i])) ** t) ** (1/t)
print(round(abs((abs(a) - abs(b)), 7)))	
