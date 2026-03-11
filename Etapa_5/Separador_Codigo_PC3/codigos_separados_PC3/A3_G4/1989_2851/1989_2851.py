x = input("Digite o nome do aminoacido: ")
x = x.upper()

o = 15.999
c = 12.011
n = 14.00674
h = 1.00794
peso_molecular = 0

if( x == "ASPARAGINA"):
	peso_molecular = (c*4) + (h*8) + (n*2) + (o*3)
	print(round(peso_molecular, 2))
elif( x == "GLUTAMINA"):
	peso_molecular = (c*5) + (h*8) + n + (o*4)
	print(round(peso_molecular, 2))
elif( x == "TRIPTOFANO"):
	peso_molecular = (c*11) + (h*11) + (n*2) + (o*2)
	print(round(peso_molecular, 2))
else:
	print("Entrada: " ,x)
	print("Dado Invalido")
	