nom = input("nome do aminoacido: ")
o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079

if (nom == "Histidina".lower()):
	x=(c*6)+(h*10)+(n*3)+(o*2)
	print(round(x,2))
elif (nom == "Leucina".lower()):
	x=(c*6)+(h*13)+(n)+(o*2)
	print(round(x,2))
elif (nom == "Lisina".lower()):
	x=(c*6)+(h*15)+(n*2)+(o*2)
	print(round(x,2))
else:
	print("Entrada:", nom.lower())
	print("Dado Invalido")
	