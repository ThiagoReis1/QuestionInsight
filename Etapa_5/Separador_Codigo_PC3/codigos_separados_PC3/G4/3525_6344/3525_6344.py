from math import*

x = float(input("Digite um numero: "))
k = int(input("Digite a quantidade de termos da serie: "))

cont = 0
senh = 0

while (cont < k):
	senh = senh + (x ** k) / factorial(k)
	cont = cont + 1
print(cont)
	
