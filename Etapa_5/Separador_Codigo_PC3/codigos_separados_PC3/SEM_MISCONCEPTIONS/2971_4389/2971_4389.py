j = float(input("Informe a taxa de juros:\n"))
valor = float(input("Informe o valor do imovel:\n"))
qf = 1500*(((1+j))**36)

if(qf >= valor):
	
	print(round(qf,2))
	print("Sim")
else:
	
	print(round(qf,2))
	print("Nao")