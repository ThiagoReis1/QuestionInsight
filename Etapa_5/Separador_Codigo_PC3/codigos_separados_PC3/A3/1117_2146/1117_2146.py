preco = float(input("Preco normal: "))
dia = int(input("Dia da semana: "))
musica = input("Musica ao vivo? ")
taxa = 20
domingo = 1
segunda = 2
terça = 3
quarta = 4
quinta = 5
sexta = 6
sabado = 7

if(dia == 1 and dia == 3 and dia == 5 and musica == "N"):
	print(preco, dia, musica)
	print(preco - ((25 / 100)* preco))
	
if(dia == 1 and dia == 3 and dia == 5 and musica == "S"):
	print("Entradas: ", preco, dia, musica)
	print("Valor a pagar: ", preco + taxa)
	