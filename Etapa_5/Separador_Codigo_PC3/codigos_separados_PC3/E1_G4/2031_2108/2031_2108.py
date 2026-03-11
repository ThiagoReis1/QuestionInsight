n = int(input("Digite um numero:"))
soma = 0
while (n != -1):
	if(n == 1 or 2 or 3 or 4 or 5 or 6):
		soma = soma + n
		n = int(input("Digite um numero:"))
		print(soma)