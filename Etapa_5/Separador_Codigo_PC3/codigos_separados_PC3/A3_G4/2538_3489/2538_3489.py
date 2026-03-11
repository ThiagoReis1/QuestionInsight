S = float(input("valor do sitio: "))
D = float(input("deposito inicial: "))
M = float(input("deposito mensal: "))
j = float(input("taxa de juros: "))

d = D
tempo = 0
soma = 0
fim = S

if (S > 0 and d > 0 and M > 0 and j > 0):
	while ( d < fim):
		d = d + (d * j/100) + M
		tempo = tempo + 1
	print(tempo)
else:
	print("Dados incorretos")