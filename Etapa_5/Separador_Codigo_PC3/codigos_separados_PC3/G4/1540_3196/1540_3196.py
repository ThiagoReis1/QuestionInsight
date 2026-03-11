from math import*
x = float(input("Insira o numero: "))
k1 = int(input("Numero de repeticoes: "))
c = 1 
s = 1
l = 1
while(c<=k1):
	s = s +((-1)**(c+1))*((x**l)/factorial(l))
	l = l + 2
	c = c + 1 
print(round(s, 6))