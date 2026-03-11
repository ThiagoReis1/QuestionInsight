def contagem_regressiva(N):
	for i in range(N, 9, -1):
		print(i)
	print("Fim da contagem regressiva!")
	
N = int(input("Digite um número inteiro positivo: "))

if N > 10:
	contagem_regressiva(N)
else:
	print("O número digitado precisa ser maior que 10.")