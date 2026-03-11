mol = input("").lower()
O = 15.999
C = 12.011
N = 14.00674
H = 1.00794
if ((mol == "glutamina") or (mol == "histidina") or (mol == "prolina")):
	if ((mol == "glutamina")):
		peso = C*5 + H*8 + N*1 + O*4
		print(round(peso, 2))
	if (mol == "histidina"):
		peso = C*6 + H*10 + N*3 + O*2
		print(round(peso, 2))
	if (mol == "prolina"):
		peso = C*5 + H*10 + N + O*2
		print(round(peso, 2))
else:
	print("Entrada:", mol)
	print("Dado Invalido")