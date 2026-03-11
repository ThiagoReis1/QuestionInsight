p = float(input("preco do ingresso normal"))
d = int(input("dia da semana"))
m = input("musica ao vivo")
domingo = 1
segunda =2
terca = 3
quarta = 4
quinta = 5
sexta = 6 
sabado = 7
n = 20.00
e1 = (p)*0.75
e2 = (p)*0.75+n
e3 = (p)
e4 = (p+n)
if((p>0) and (d>0 and d<=7) and (m == "S" or m == "N")):
	if((d == 1) and (m == "S")):
		print("Entradas:",p, "," ,d, "," ,m )
		print("Valor a pagar:R$", round(e4,2))
	elif((d == 2) and (m == "S")):
		print("Entradas:",p, "," ,d, "," ,m )
		print("Valor a pagar:R$", round(e2,2))
	elif((d == 3) and (m == "S")):
		print("Entradas:",p, "," ,d, "," ,m )
		print("Valor a pagar:R$", round(e4,2))
	elif((d == 4) and (m == "S")):
		print("Entradas:",p, "," ,d, "," ,m )
		print("Valor a pagar:R$", round(e4,2))
	elif((d == 5) and (m == "S")):
		print("Entradas:",p, "," ,d, "," ,m )
		print("Valor a pagar:R$", round(e4,2))  
	elif((d == 6) and (m == "S")):
		print("Entradas:",p, "," ,d, "," ,m )
		print("Valor a pagar:R$", round(e4,2))
	elif((d == 7) and (m == "S")):
		print("Entradas:",p, "," ,d, "," ,m )
		print("Valor a pagar:R$", round(e4,2))
else:
	print("Entradas:",p, "," ,d, "," ,m )
	print("Dados invalidos")

