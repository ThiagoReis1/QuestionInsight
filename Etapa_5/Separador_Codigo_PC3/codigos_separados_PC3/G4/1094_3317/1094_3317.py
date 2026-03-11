from math import*
n = int(input("numero fornecido: "))
n1 = n // 1000
n2 = n % 1000

calculo = (n1 + n2)**2
if(calculo == n):
	msg = "atende"
else:
	msg = "nao atende"
print(msg)
print(n)