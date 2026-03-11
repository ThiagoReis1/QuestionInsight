n = int(input("Digite um numero inteiro: "))
if n >=1:
	if n%3 == 0 and n%5 == 0:
		print("Zuuum")
	elif n%3 == 0:
		print("Plunct")
	elif n%5 == 0:
		print("Plact")
	else:
		print(n)