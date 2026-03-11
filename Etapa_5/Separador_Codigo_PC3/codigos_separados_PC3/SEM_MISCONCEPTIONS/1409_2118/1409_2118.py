ataque = input("ataque: ")
d1 = int(input("valor: "))
d2 = int(input("valor: "))
d3 = int(input("valor: "))
d4 = int(input("valor: "))

espada = (d1 + 6) + (d2 + 6) + (d3 + 6) + (d4 + 6)
cauda =  (d1 + d2 + d3) * d4

if (ataque == "espada"):
	print(espada)

else:
	print(cauda)