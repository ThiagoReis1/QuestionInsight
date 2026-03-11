
numero = int(input("Digite um numero inteiro: "))

quociente = numero // 47

resto = numero % 47

if (resto == 0):
	print(quociente)
	print("sim")

else:
	print(resto)
	print("nao")