aminoacido = input("Nome do aminoacido:")

O = 15.999
C = 12.011
N = 14.00674
H = 1.00794

if(aminoacido.lower() == "glutamina"):
	glutamina = (5*C)+(8*H)+(1*N)+(4*O)
	print(round(glutamina, 2))

elif(aminoacido.lower() == "histidina"):
	histidina = (6*C)+(10*H)+(3*N)+(2*O)
	print(round(histidina, 2))

elif(aminoacido.lower() == "prolina"):
	prolina = (5*C)+(10*H)+N+(2*O)
	print(round(prolina, 2))

else:
	print("Entrada:", aminoacido)
	print("Dado Invalido")