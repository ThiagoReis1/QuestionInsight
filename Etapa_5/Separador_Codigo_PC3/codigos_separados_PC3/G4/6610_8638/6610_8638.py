num = int(input("numero: "))
cont = 1
soma = 0
while cont <= num:
	if num % 2 == 0:
		soma = soma + 1
	cont = cont + 1
print("soma=", soma)