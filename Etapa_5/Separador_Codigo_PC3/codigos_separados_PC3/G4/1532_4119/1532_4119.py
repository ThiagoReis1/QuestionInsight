from math import* 
x = float(input("digite um numero: "))
k = int(input("quantidade de termos: "))
e = 0 #variavel acumuladora
cont = 0 #variavel contadora
fact = 1 #variavel acumuladora
while (cont < k):
	e = e + (x / factorial(fact))
	x = x * (x ** 2)
	fact = fact + 2
	cont = cont + 1
print (round(e , 9))