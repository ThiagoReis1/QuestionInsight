from math import factorial 

x = float(input("Numero real para x: "))
k = int(input("Numero inteiro para k: "))

soma = 0
cont = 0
quant = 0

while (quant < k):
	p = (x ** cont) / (factorial(cont))
	cont = cont + 2
	soma = soma + p
	quant = quant + 1
	
if(cont >= k):
	print(round(soma, 8))