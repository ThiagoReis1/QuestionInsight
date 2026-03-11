C = float(input("Digite o valor da casa: "))
D = float(input("Digite o valor inicial: "))
M = float(input("Digite o deposito mensal: "))
J = float(input("Digite a taxa de juros: "))
tempo = 0
J = J / 100
meses = 0
while tempo > 0:
	if C > 0 and D > 0 and M > 0 and J > 0:
		meses = D + M*meses 
		tempo = meses*J
		meses = meses + 1
		print(round(tempo,2))
else:
	print("Dados incorretos")
	
