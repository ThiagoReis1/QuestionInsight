preco_normal= float(input("preco da entrada: "))
dia_semana = int(input("qual o dia da semana?" ))
musica_aovivo = input("É dia de música ao vivo? (S)(N):")
print("Entradas:",preco_normal,",",dia_semana,",",musica_aovivo)
if (preco_normal< 0):
	print("Dados invalidos")
elif (dia_semana == 2)or(dia_semana == 3)or(dia_semana == 5):
	total = preco_normal - 0.25
elif (musica_aovivo == "S"):
	total = preco_normal + 20
else:
	total = preco_normal
print(round(total, 2)