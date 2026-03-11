preco = float(input("Preco normal da entrada : "))
dia = int(input("Dia da semana: "))
aovivo = input("Eh dia de musica ao vivo: ")

ao_vivo = aovivo.upper()

print("Entradas: ", preco, ",", dia, ",", aovivo)

if ((preco >= 0) and (1 <= dia <= 7) and ((ao_vivo == "S") or (ao_vivo == "N"))):
	if (((dia == 2)or(dia == 3)or(dia == 5)) and (ao_vivo == "N")):
		final = preco * 0.75
	elif (((dia == 2)or(dia == 3)or(dia == 5)) and (ao_vivo == "S")):
		final = (preco * 0.75) + 20
	elif (((dia == 1) or (dia == 4) or (dia == 6) or (dia == 7)) and (ao_vivo == "N")):
		final = preco
	elif (((dia == 1) or (dia == 4) or (dia == 6) or (dia == 7)) and (ao_vivo == "S")):
		final = preco + 20
	
	print("Valor a pagar: R$ ", round(final,2))

else:
	print("Dados invalidos")
		