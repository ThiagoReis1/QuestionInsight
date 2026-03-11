from math import*
x = eval (input ("digite o angulo: "))
k = int (input ("insira a quantidade de termos: "))
a = 0
n = 0
s = 1
while (k > 0):
	a = a + s * ((x ** n) / (factorial (2*n)))
	n = n + 1
	s = -s
	k = k - 1
print (round (a, 6))