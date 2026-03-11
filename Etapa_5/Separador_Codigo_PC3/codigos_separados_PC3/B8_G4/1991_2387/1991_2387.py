amino = input("").upper()

O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

if((amino != "GLICINA")and(amino != "PROLINA") and(amino !="SERINA")):
	print("Entrada:",amino)
	print("Dado Invalido")
elif(amino == "GLICINA"):
	a = (2*C)+(5*H)+N+(2*O)
	b = round(a, 2)
	print(b)
elif(amino == "PROLINA"):
	a = (5*C)+(10*H)+N+(O*2)
	b = round(a, 2)
	print(b)	
elif(amino == "SERINA"):
	a = (3*C)+(7*H)+N+(3*O)
	b = round(a, 2)
	print(b)	