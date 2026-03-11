a = input("nome do aminoacido: ").upper()
c = 12.011
h = 1.00794
n = 14.00674
o = 15.999
ASPARAGINA = (c*4) + (h*8) + (n*2) + (o*3)
GLUTAMINA = (c*5) + (h*8) + (n) + (o*4)
TRIPTOFANO = (c*11) + (h*11) + (n*2) + (o*2)

if(a=="ASPARAGINA"):
 	print(round(ASPARAGINA,2))
elif(a=="GLUTAMINA"):
	print(round(GLUTAMINA,2))
elif(a=="TRIPTOFANO"):
	print(round(TRIPTOFANO,2))
else:
	print("Entrada: ",a)
	print("Dado Invalido")

