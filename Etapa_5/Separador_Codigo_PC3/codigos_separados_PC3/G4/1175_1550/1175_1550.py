from math import sqrt
n= int(input("digite o valor de n: "))
i=0
soma=0
if(n>0):
	while(i>n):
		soma= soma+((-1)**i*(sqrt(i+1)/(6+2*i+3)))
		i= i + 1
else:
	print("valor invalido")
print(soma)