# faça seu código aqui!

qtpizza = int(input("Quantidade de pizzas encomendadas? "))

if qtpizza < 3:
	valor = (qtpizza*5)+3
	print("total= ",round(valor,2))
elif qtpizza == 3:
	valor = (qtpizza*5)+3.25
	print("total= ", round(valor,2))
else:
	valor = (qtpizza*5)+4.5
	print("total= ", round(valor,2))