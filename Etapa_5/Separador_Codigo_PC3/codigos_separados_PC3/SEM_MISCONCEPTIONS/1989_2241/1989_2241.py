nome = input("aminoacido: ")
o = 15.999
c = 12.011
n = 14.00674
h = 1.00794
ASPARAGINA = ((c*4) + (h*8) + (n*2) + (o*3))
GLUTAMINA = ((c*5) + (h*8) + (n*1) + (o*4))
TRIPTOFANO = ((c*11) + (h*11) + (n*2) + (o*2))

if(nome == "asparagina".upper()):
	print(round(ASPARAGINA, 2))
elif(nome == "glutamina".upper()):
	print(round(GLUTAMINA, 2))
elif(nome == "triptofano".upper()):
	print(round(TRIPTOFANO, 2))
else:
	print("Entrada: X")
	print("Dado Invalido")
