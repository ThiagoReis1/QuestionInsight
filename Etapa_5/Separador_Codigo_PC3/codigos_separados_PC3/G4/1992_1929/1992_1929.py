aminoacido = input("nome do aminoacido: ").lower()
O = 15.999
C = 12.011
N = 14.00674
H = 1.00794
if (aminoacido == "glutamina"):
	peso = (C*5) + (H*8) + (N*1) + (O*4)
	print(round(peso, 2))
elif (aminoacido == "histidina"):
	peso = (C*6) +(H*10) + (N*3) + (O*2)
	print(round(peso, 2))
elif (aminoacido == "prolina"):
	peso = (C*5) + (H*10) + N + (O*2)
	print(round(peso, 2))
else:
	print("Entrada:", aminoacido)
	print("Dado Invalido")

