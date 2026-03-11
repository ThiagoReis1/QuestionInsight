N = int(input("Digite o numero inteiro: "))

if N < 0:
	print("nao e positivo")
else:
	for i in range(N, 9, -1):
		print(i)
	print("Fim da contagem regressiva!")
	