#UNIVERSIDADE FEDERAL DO AMAZONAS
#LETICIA DANTAS DE OLIVEIRA - 21601436
#21/07/2016
#EXERCICIO 01

precoN = float(input("Preco normal: "))
dia = int(input("Dia da semana: "))
musica = input("Musica ao vivo? ")

if (musica == "S"):
	preco = precoN + 20.0
	print("Entradas:", precoN, ",", dia, ",", musica)
	print("Valor a pagar: R$", round(preco, 2))
elif ( dia == 2) or (dia == 3) or (dia == 5):
	desconto = precoN * 0.25
	preco = precoN - desconto
	print("Entradas:", precoN, ",", dia, ",", musica)
	print("Valor a pagar: R$",round(preco, 2))
elif (musica == S) and (dia == 2) or (dia == 3) or (dia == 5):
	desconto = precoN * 0.25
	precod = (precoN - desconto) + 20.0
	print("Valor a pagar: R$", round(precod, 2))
else :
	print("Entradas:", precoN, ",", dia, ",", musica)
	print("Dados invalidos")