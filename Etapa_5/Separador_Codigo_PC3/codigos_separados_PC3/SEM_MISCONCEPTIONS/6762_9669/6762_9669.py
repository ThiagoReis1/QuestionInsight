# faça seu código aqui!
idade = int(input("Entre com a idade: "))
ingresso = 20
if idade < 12:
	taxa = 1.25
	valor_total = ingresso + taxa
	print(float(round(valor_total,2)))
	
elif idade == 12:
	taxa = 2.25
	valor_total = ingresso + taxa
	print(float(round(valor_total,2)))
	
else:
	taxa = 3.25
	valor_total = ingresso + taxa
	print(float(round(valor_total,2)))