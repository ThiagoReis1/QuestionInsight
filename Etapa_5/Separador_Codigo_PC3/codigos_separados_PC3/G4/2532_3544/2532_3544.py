c = float(input("Digite o valor do carro: "))
d = float(input("Digite o valor inicial depositado: "))
m = float(input("Digite o deposito mensal fixo: "))
j = float(input("Digite a taxa de juros: "))
t = 0
saldo = m
tempo = 0
while (saldo < c):
	t = t + 1
	saldo = (saldo + d) + (saldo + d) * (j / 100)
	print(saldo)
	tempo = tempo + 1

print(tempo)
