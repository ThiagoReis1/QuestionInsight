pecasdeouro = int(input("inserir pecas de ouro: "))
armadura = input("insira a armadura: ").upper()
d = int(input("insira a destreza: "))

if(armadura == "INTEIRA" and pecasdeouro >= 200 and d>=1 and d<=8):
	print(30*d-20)
elif(armadura == "MALHA" and pecasdeouro >= 50 and pecasdeouro <100 and d>=1 and d<=8):
	print(15*d-1)
elif(armadura == "PLACA" and pecasdeouro >=100 and pecasdeouro <200 and d>=1 and d<=8):
	print(20*d-18)
elif(pecasdeouro<50):
	print("PO insuficiente")
elif(d<1 and d>8):
	print("Entrada invalida")