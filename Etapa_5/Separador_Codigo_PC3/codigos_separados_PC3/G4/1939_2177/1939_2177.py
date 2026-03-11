nome=input("Leia o nome: ")
o = 15.999
c = 12.011
n = 14.00674
h = 1.00794


if(nome.upper() == "ASPARAGINA"):
	Asp = (c*4) + (h*8) + (n*2) + (o*3)
	print(round(Asp,2))
else:
	trip = c*11 + h*11 + n*2 + o*2
	print(round(trip,2))
	