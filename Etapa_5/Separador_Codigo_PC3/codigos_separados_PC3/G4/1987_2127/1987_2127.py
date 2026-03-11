ami = input("Digite o amino acido:")
O = float(15.999)
C = float(12.011)
N = float(14.00674)
H = float(1.00794)
if(ami.upper() != "ALANINA" and ami.upper() != "VALINA" and ami.upper() != "TIROSINA"):
	print("Entrada:", ami)
	print("Dado Invalido")
elif(ami.upper() == "ALANINA"):
	M = (3*C)+(7*H)+(1*N)+(2*O)
	print(round(M,2))
elif(ami.upper() == "VALINA"):
	M = (5*C)+(11*H)+(1*N)+(2*O)
	print(round(M,2))
else:
	M = (9*C)+(11*H)+(1*N)+(3*O)
	print(round(M,2))
