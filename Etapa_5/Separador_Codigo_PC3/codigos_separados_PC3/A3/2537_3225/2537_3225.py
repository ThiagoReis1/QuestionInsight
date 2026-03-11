V = float(input("Digite o valor da heranca:"))
M = float(input("Digite o valor do saque:"))
j = float(input("Digite a taxa de juros:"))

juros = j/100
saldo = V * j
tempo = 0

if((V > 0) or (M > 0) or (j > 0)):
	while (saldo > saldo + 20/100):
	
		rend = saldo - M
		tempo = tempo + 1

	
else:
	print("Dados incorretos")
print(tempo)