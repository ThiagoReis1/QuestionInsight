preco = float(input("preco: "))
dia = int(input("iufh: "))
musica = input("sauh: ").upper()

print("Entradas: ", preco,",", dia,",", musica)


if preco >= 0 and (dia >= 1 and dia <= 7) and (musica == "S" or musica == "N"):
	if (dia == 2 or dia == 3 or dia == 5) and musica == "N":
		precos = preco - (preco * 0.25)
		
	elif (dia == 2 or dia == 3 or dia == 5) and musica == "S":
		precos = (preco - (preco * 0.25)) + 20
	else:
		if (dia != 2 or dia != 3 or dia != 5) and musica == "S":
			precos = preco + 20
		else:
			precos = preco
	print("Valor a pagar: R$ ", round(precos,2))
else:
	print("Dados invalidos")