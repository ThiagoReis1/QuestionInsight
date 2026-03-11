inteiro = int(input("Digite um numero inteiro: "))
divisao = inteiro//17
resto = inteiro % 17

if (resto == 0):
	print(divisao)
	print("sim")
	
else:
	print(resto)
	print("nao")