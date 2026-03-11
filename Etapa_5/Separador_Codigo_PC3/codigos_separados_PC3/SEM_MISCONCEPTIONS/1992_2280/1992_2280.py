nome = input("aminoacido:").lower()
o = 15.999
c = 12.011
n = 14.00674
h = 1.00794
glutamina = ((c*5)+(h*8)+(n*1)+(o*4))
histidina = ((c*6)+(h*10)+(n*3)+(o*2))
prolina = ((c*5)+(h*10)+(n)+(o*2))
if(nome == "glutamina"):
	print(round(glutamina,2))
elif(nome=="histidina"):
	print(round(histidina,2))
elif(nome=="prolina"):
	print(round(prolina,2))
else:
	print("Entrada:",nome)
	print("Dado Invalido")