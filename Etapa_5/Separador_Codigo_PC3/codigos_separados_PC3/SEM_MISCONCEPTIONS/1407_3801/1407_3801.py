vida_inicial = int(input("vida: "))
d1 = int(input("valor: "))
d2 = int(input("valor: "))
d3 = int(input("valor: "))
n = 10 * (d1 + d2 + d3)
pontosdevidarestante = vida_inicial - n

if(pontosdevidarestante > 0):
	mensagem = input("VIVO")
else:
	mensagem = input("MORTO")
	print (mensagem)