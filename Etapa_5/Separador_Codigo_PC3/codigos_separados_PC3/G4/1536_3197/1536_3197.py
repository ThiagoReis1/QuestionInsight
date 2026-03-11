from math import *
x = eval(input("Insira o angulo:"))
k = int(input("Numero de repeticoes:"))
g = 1
m = 0
l = 1
while (g<=k):
	m = m + ((-1)**(g+1))*((x**l)/(l))
	l = l + 1
	g = g + 1
print(round(m, 10))