po = int(input("Digite uma quantidade de PO: "))
armadura = input("Digite um nome: ")
d = int(input("Digite um numero de destreza: "))

f1 = 30 * d - 20
f2 = 15 * d -1
f3 = 20 * d - 18

if ((d < 1 or d > 8) or ((armadura != "INTEIRA") and (armadura != "MALHA") and (armadura != "PLACA"))):
	print("Entrada invalida")
elif (po < 50):
	print("PO insuficiente")
elif ((po >= 50 and po < 100) and (armadura == "MALHA")):
	print(f2)
elif ((po >= 100 and po < 200) and (armadura == "PLACA")):
	print(f3)
elif ((po >= 200) and (armadura == "INTEIRA")):
	print(f1)
	