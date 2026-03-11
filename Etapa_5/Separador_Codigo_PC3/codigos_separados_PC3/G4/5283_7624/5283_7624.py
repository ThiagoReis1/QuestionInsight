num = int(input("digite o numero: "))

cont = 0
soma = 0 

while (num != 0):
	if (num > 0):
		soma = soma +1
	cont = cont + 1
	num = int(input("digite o numero: "))
print(cont)
print(round(soma / cont * 100, 2))
	
		