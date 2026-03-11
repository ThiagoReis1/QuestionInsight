aminoacido = input("Digite o aminoacido: ")

o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079


if(aminoacido.upper() == "GLICINA" or aminoacido.upper() == "PROLINA" or aminoacido.upper() == "SERINA"):
	if(aminoacido.upper() == "GLICINA"):
		peso_molecular =  (c * 2) + (h * 5) + n + (o * 2)
	elif(aminoacido.upper() == "PROLINA"):
		peso_molecular = (c * 5) + (h * 10) + (n) + (o * 2)
	else:
		peso_molecular = (c * 3) + (h * 7) + n + (o * 3)
		
	print(round(peso_molecular,2))
else:
	print("Entrada: ", aminoacido.upper())
	print("Dado Invalido")
	
	
