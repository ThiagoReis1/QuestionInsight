aminoacido = input("escolha o aminoacido: ")
#print("Entrada:", aminoacido.upper())
o = 15.9994
c = 12.011
n = 14.00674
h = 1.00794
if(aminoacido.upper() == "ARGININA"):
	peso = ((c*6) + (h*15) + (n*4) + (o*2))
	print(round(peso, 2))
elif(aminoacido.upper() == "TIROSINA"):
	peso = ((c*9) + (h*11) + (n*1) + (o*3))
	print(round(peso, 2))
elif(aminoacido.upper() == "TRIPTOFANO"):
	peso = ((c*11) + (h*11) + (n*2) + (o*2))
	print(round(peso, 2))
else:
	print("Entrada: ", aminoacido)
	print("Dado Invalido")