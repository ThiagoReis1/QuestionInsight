from numpy import*
from math import*

p = float(input("Insira: "))
x = array(eval(input("Insira o vetor1: ")))
y = array(eval(input("Insira o vetor2: ")))

t = p / (p-1)
n = 0

for i in range(size(x)):
	n = abs(x[i] + y[i]) ** t + n
n = (n)**(1/t)
print(round(n,5))