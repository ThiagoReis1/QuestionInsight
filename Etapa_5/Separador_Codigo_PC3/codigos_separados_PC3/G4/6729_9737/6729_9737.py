x =  int(input("Insira o Numero: "))

if x % 41 == 0:
	print(x//41)
	print("sim")
else:
	print(x%41)
	print("nao")