from math import*
x = eval(input(""))
v = int(input(""))

z =0
b = 0
indice = 1
i = 0
while(i<v):
	z = z+(indice)*(x**(b)/factorial(b))
	indice=-indice
	b= b+2
	i=i+1
print(round(z,10))