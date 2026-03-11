nda = input("aminoacido: ")
o = 15.999
c = 12.011
n = 14.00674
h = 1.00794
if (nda.lower() == "glutamina"):
	pm = (c*5)+(h*8)+(n*1)+(o*4)
	print(round(pm, 2))
elif (nda.lower() == "histidina"):
	pm = (c*6)+(h*10)+(n*3)+(o*2)
	print(round(pm, 2))
elif(nda.lower() == "prolina"):
	pm = (c*5)+(h*10)+(n*1)+(o*2)
	print(round(pm, 2))
else:
	print("Entrada:", nda)
	print("Dado Invalido")
	