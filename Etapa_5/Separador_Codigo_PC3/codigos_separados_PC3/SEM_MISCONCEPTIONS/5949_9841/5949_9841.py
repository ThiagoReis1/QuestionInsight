item = str(input("Digite [C] para croissant ou [B] para fatia de bolo: ")).upper()
quantidade = int(input("Quantidade de bolo ou croissant: "))
capp = int(input("Cappuccinos: "))
if item == "C":
	preco = (quantidade*6)+ (capp*5.5)
	print(round(preco, 1))
if item == "B":
	preco = (quantidade*3) + (capp*5.5)
	print(round(preco, 1))
	