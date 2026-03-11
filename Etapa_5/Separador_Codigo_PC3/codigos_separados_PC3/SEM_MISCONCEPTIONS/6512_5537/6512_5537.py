qtd = float(input("Digite a quantidade de duplas delicioosas que voce deseja: "))
valor = 32.90
if(qtd > 3):
	total = (valor * qtd) * 0.8
	print(round(total,2))
else:
	total = valor * qtd
	print(round(total,2))