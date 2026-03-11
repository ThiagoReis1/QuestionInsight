# Monalisa Pereira 21600560
# 140716
# Av 03 - Ex 01

preco = float(input("Insira o preço normal da entrada: "))
dia = int(input("Insira o dia da semana: "))
musica = str(input("Dia de música ao vivo? (S/N)"))

print("Entradas: ", preco, ", ", dia, ", ", musica)

if (preco>=0) and (dia>=1) and (dia<=7) and ((musica=="S") or (musica=="N")):
	if (dia==2) or (dia==3) or (dia==5):
		entrada = (preco/100) * 75
	else:
		entrada = preco
	if (musica=="S"):
		entrada = entrada+20
	else:
		entrada = entrada
	print("Valor a pagar: R$ ", (round(entrada,2)))
else:
	print("Dados invalidos")
	
	