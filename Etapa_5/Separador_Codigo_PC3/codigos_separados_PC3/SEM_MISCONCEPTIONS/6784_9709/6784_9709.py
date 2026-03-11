num = int(input("Digite um numero inteiro: "))
pais = input("Digite B ou R: ").upper()

if pais == "B":
	idade = 2023 - num
	idade_minima = 21
	if idade >= idade_minima:
		print("sim")
		print(idade - idade_minima)
	else:
		print("nao")
		print(idade_minima - idade)
else:
	if pais == "R":
		idade = 2023 - num
		idade_minimaR = 18
		if idade >= idade_minimaR:
			print("sim")
			print(idade - idade_minimaR)
		else:
			print("nao")
			print(idade_minimaR - idade)
	else:
		print("invalido")
