preco_entrada = float(input("Valor da entrada: "))
dia = input("Dia da semana: ")
musica = str(input("Musica ao vivo? "))
if (dia == "2" or dia == "3" or dia == "5"):
	total = preco_entrada - (preco_entrada * 0.25)
else:
	total = preco_entrada
if (musica == "S"):
	valor = total + 20
else:
	valor = total
print("Entradas:",preco_entrada,",",dia,",",musica)
print(round("s"valor,2))