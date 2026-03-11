# faça seu código aqui!

qtd = int(input("Digite a quantidade de pizzas: "))

if	qtd < 3:
	total = qtd * 5.00 + 3.00
elif	qtd == 3:
	total = qtd * 5.00 + 3.25
elif	qtd > 3:
	total = qtd * 5.00 + 4.50
	
print(round(total, 2))