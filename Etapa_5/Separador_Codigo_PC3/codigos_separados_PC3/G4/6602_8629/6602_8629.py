# faça seu código aqui!
numero = int(input("numero: "))
cont = 0
P = 0
C = 0
L = 0
while (cont < numero):
	voto = input("l , c ou p: ")
	cont = cont + 1
	
	if(voto.upper() == "L"):
		L = L + 1
	if(voto.upper() == "C"):
		C = C + 1
	if(voto.upper() == "P"):
		P = P + 1
		

	
print("L=", L)
print("C=", C)
print("P=", P)