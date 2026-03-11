from math import*
x= eval(input("Angulo: "))
k= int(input("Termos: "))

soma= 1
cont1= 1
cont2= 2

while(cont1 < k):
	soma = soma + ((-1) ** cont1) * ((x ** cont1) / factorial(cont2))
	cont1= cont1 + 1
	cont2= cont2 + 2
print(round(soma, 6))