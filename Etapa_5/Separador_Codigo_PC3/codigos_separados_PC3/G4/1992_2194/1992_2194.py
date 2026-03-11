mol = input("").lower()
o = 15.999
c = 12.011
n = 14.00674
h = 1.00794
if ((mol == "glutamina") or (mol == "histidina") or (mol == "prolina")):
	if ((mol == "glutamina")):
		peso = (c*5 + h*8 + n*1 + o*4)
		print(round(peso, 2))
	if ((mol == "histidina")):
		peso = (c*6 + h*10 + n*3 + o*2)
		print(round(peso, 2))
	if ((mol == "prolina")):
		peso = (c*5 + h*10 + n + o*2)
		print(round(peso, 2))
else:
	print("Entrada:", mol)
	print("Dado Invalido")

