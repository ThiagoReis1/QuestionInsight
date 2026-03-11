numero = int(input("Digite um numero inteiro: "))

if numero %37 == 0:
	quociente = numero // 37
	print(quociente)
	print("sim")
	
else: 
	resto = numero %37
	print(resto)
	print("nao")