entrada = input("Digite o aminoacido:")

O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

if((entrada.upper() == "GLICINA") or (entrada.upper() == "PROLINA") or (entrada.upper() == "SERINA")):
	if(entrada.upper()  == "GLICINA"):
		peso_molecular = (C * 2) + (H * 5) + (N) + (O * 2)
	
	elif(entrada.upper()  == "PROLINA"):
		peso_molecular = (C * 5) + (H * 10) + (N) + (O * 2)
	
	else:
		peso_molecular = (C * 3) + (H * 7) + (N) + (O * 3)
	
	print(round(peso_molecular, 2))
else:
	print("Entrada:", entrada.upper())
	print("Dado Invalido")
	
