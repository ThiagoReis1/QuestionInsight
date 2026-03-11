from numpy import*
from math import*
p = float(input("Informe o valor de p maior que 1: "))
x = array(eval(input("Vetor1 :")))
y = array(eval(input("Vetor2 :")))
t = p/(p-1)
x0 = 0
y0 = 0
for i in range(size(x)):
	x0 = (abs(x[i]))**t + x0
x1 = x0 ** 1/t
for j in range(size(y)):
	y0 = (abs(y[j]))**t + y0
y1 = y0 ** 1/t
sm = 2*x1 - y1
print(round(sm,4))