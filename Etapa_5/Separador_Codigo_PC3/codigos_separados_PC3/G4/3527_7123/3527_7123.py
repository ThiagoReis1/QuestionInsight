from math import*

x= float(input("digite o numero real:"))
y= int(input("digite um numero inteiro:"))
cont = 0
acum = 0
i = 0

while (cont < y):
	acum = acum + (x**i/factorial (i))
	i = i + 1
	cont = cont + 1
print(round(acum,9))