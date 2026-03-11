from math import*

x = eval(input("digite um angulo: "))
k = int(input("digite um numero inteiro: "))

cont = 1
acum = 1

while(cont < k):
	acum = acum + (-1)**(cont) * (x**(2*cont))/ factorial(2*cont)
	cont = cont + 1
	
print(round(acum, 10))
