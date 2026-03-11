item = input("Voce deseja bolo ou salgado? (B/S) ")
qtd = int(input("Digite a quantidade desejada: "))
qtdcappuccino = int(input("Digite a quantidade de cappuccinos: "))
bolo = 5
salgado = 4
cappuccino = 7.5
if(item.upper() == "B"):
	total = qtd*5 + qtdcappuccino*7.5
	print(round(total,2))
else:
	total = qtd*4 + qtdcappuccino*7.5
	print(round(total,2))