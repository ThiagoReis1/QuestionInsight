from math import*
x = eval(input("digite: "))
k = int(input("digite: "))
soma = 0
cont1 = 0
cont2 = 0
while (cont1 < k):
	soma = soma + ((-1) ** cont1) * (x ** (cont2)) / (factorial(cont2))
	cont1 = cont1 + 1
	cont2 = cont2 + 2 
print(round(soma, 10))