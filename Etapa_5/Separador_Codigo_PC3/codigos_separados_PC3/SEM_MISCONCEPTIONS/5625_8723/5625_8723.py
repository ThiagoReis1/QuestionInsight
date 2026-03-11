tapisoca = input("Salgado ou tapioca?: ")
quanti = int(input("Quantidade de tapioca ou salgado: "))
acai = int(input("Quantidade de acai: "))

if(tapisoca == "T"):
	x = quanti*5.50+acai*10.00
	print(round(x,1))
	
else:
	z = quanti*4.00+acai*10.00
	print(round(z,1))