opcao = input("Qual sera a sua escolha? (B/C)  ")

if opcao.upper() == "B":
	bolos = int(input("Quantas fatias de bolo? "))
	capuccino = int(input("Quantos capuccinos? "))
	valorfodass = (bolos*3)+(capuccino*5.50)
	print(round(valorfodass,2))
	
if opcao.upper() == "C":
	cross = int(input("Quantos crossaints? "))
	capuccino = int(input("Quantos capuccinos? "))
	valorfodass = (cross*6)+(capuccino*5.50)
	print(round(valorfodass,2))
