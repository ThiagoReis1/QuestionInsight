# Leitura das informações

consumo = int(input("Qual o consumo de agua?"))

# Saída
if consumo < 10:
	preco_1 = 20 + 2*consumo
	print(round(preco_1,2))
if consumo >= 10 and consumo<20:
	preco_2 = 20 + 2.5*consumo
	print(round(preco_2,2))
if consumo>=20 and consumo<40:
	preco_3 = 20 + 2.75*consumo
	print(round(preco_3,2))
if consumo >=40:
	preco_4 = 20 + 3*consumo
	print(round(preco_4,2))