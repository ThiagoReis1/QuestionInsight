preco = float(input("digite o preco: "))
dia = int(input("digite o dia da semana: "))
musical = input("S ou N:")

if ( dia == 1) or (dia == 4) or (dia == 6) or (dia == 7):
	if ( musical == "S"):
		total = preco + 20
	else:
		total = preco
elif ( dia == 2) or (dia == 3) or (dia == 5):
	if ( musical == "S"):
		total =(preco + 20) * 0.25
	else:
		total = preco - ( preco * 0.25)
else:
	print("Dados invalidos")
print("Entradas:", preco, ",", dia, ",", musical)
print("Valor a pagar: R$" , round(total,2))