nasc = int(input(""))
pais = input("")
pais = pais.upper()
calcB = 2023 - nasc
calcJ = 2023 - nasc
calcApB = calcB - 18
calcApJ = calcJ - 16
calcApB2 = 18 - calcB
calcApJ2 = 16 - calcJ
if(pais != "B" and pais != "J"):
	print("invalido")
elif(pais == "B" and calcB >= 18):
	print("sim")
	print(calcApB)
elif(pais == "B" and calcB<18):
	print("nao")
	print(calcApB2)
elif(pais == "J" and calcJ >= 16):
	print("sim")
	print(calcApJ)
elif(pais == "J" and calcJ<16):
	print("nao")
	print(calcApJ2)