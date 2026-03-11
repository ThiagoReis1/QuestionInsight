numero = int(input("digite o numero: "))
x = numero // 41 

if numero % 41 == 0:
	print(x)
	print("sim")
	
else:
	print(numero % 41)
	print("nao")
	