aminoacido = input("nome: ")
aminoacido = aminoacido.upper()
o = 15.999
c = 12.011
n = 14.00674
h = 1.00794
if(aminoacido != "asparagina".upper() and aminoacido != "glutamina".upper() and aminoacido != "triptofano".upper()):
	print("Entrada:", aminoacido)
	print("Dado Invalido")
elif(aminoacido == "asparagina".upper()):
	print(round(c * 4 + h * 8 + n * 2 + o * 3,2))
elif(aminoacido == "glutamina".upper()):
	print(round(c * 5 + h * 8 + n * 1 + o * 4,2))
elif(aminoacido == "triptofano".upper()):
	print(round(c * 11 + h * 11 + n * 2 + o * 2,2))