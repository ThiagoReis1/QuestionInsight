a = input("aminoacido:").lower()
o = 15.999
c = 12.011
n = 14.00674
h = 1.00794
glutamina = c*5 + h*8 + n*1 + o*4
histidina = c*6 + h*10 + n*3 + o*2
prolina = c*5 + h*10 + n*1 + o*2
if (a == "glutamina"):
	print(round(glutamina,2))
elif (a == "histidina"):
	print(round(histidina,2))
elif (a == "prolina"):
	print(round(prolina,2))
else:
	print("Entrada:", a)
	print("Dado Invalido")