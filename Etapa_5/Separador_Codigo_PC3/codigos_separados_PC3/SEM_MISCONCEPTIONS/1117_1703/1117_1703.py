# Hanna Soares Rodrigues
# Avaliação 03
#21/07/2016

preco_normal = float(input("Preço da entrada: "))
dia = int(input("Qual o dia da semana? "))
musica = input("É dia de música ao vivo? ")

print( preco_normal,"," dia,"," musica)

if (preco_normal >= 0) and (dia <= 7) and (musica == "S" or musica == "N"):
	if (musica == "S"):
		preco_total = preco_normal + 20.00
	elif (musica == "N"):
		preco_total = preco_normal 
	elif (dia == 2) or (dia == 3) or (dia == 5):
		preco_total = preco_normal - (preco_normal * 0.25)
			if (musica == "S")
	
	else:
		preco_total = preco_normal
	if (musica == "S"):
			
			
else:
	print("Dados invalidos")
	
