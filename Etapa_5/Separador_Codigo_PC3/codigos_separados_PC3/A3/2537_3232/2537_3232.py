V = float(input("Digite o valor da heranca: "))
M = float(input("Digite o valor do saque: "))
j = float(input("Digite a taxas de juros: "))

juros = j/100

tempo = 0

while ((V > 0) and (M > 0) and (j > 0)):
	tempo = V * (juros) + M
	print(tempo)
