amac = input("Digite o amino acido:")
O = float(15.999)
C = float(12.011)
N = float(14.00674)
H = float(1.00794)
if(amac.upper() != "ASPARAGINA" and amac.upper() != "GLUTAMINA" and amac.upper() != "TRIPTOFANO"):
	print("Entrada:", amac)
	print("Dado Invalido")
elif(amac.upper() == "ASPARAGINA"):
	M = (4*C)+(8*H)+(2*N)+(3*O)
	print(round(M,2))
elif(amac.upper() == "GLUTAMINA"):
	M = (5*C)+(8*H)+(1*N)+(4*O)
	print(round(M,2))
else:
	M = (11*C)+(11*H)+(2*N)+(2*O)
	print(round(M,2))
