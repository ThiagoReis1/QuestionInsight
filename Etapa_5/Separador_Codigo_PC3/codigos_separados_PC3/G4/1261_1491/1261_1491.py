from numpy import *
p = float(input("Insira um numero real:"))
x = array(eval(input("Insira o vetor x:")))
y = array(eval(input("Insira o vetor y:")))
t = p / (p - 1)
n = 0

for i in range(size(x)):
	n = (abs(x[i] + y[i]) ** t) + n
v = n ** (1/t)
print(round(v, 5))