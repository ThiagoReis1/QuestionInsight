O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079
aminoacido = input("Nome do Aminoácido: ").lower()
histidina = C*6 + H*10 + N*3 + O*2
leucina = C*6 + H*13 + N + O*2
lisina = C*6 + H*15 + N*2 + O*2
if(aminoacido == "histidina"):
	print(round(histidina, 2))
elif(aminoacido == "leucina"):
	print(round(leucina, 2))
elif(aminoacido == "lisina"):
	print(round(lisina, 2))
else:
	print("Entrada", aminoacido)
	print("Dado Invalido")

