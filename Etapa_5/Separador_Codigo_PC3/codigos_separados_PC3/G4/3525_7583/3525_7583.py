from math import factorial

x = float(input("numero real: "))
k = int(input("numero inteiro: "))

cont = 0
soma = 0

while(cont < k):
	serie = (x ** (2*cont + 1))/factorial(2*cont +1)
	soma = soma + serie
	cont = cont + 1
print(round(soma, 9))