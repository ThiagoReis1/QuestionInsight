Z = int(input("Insira o numero de zumbis: "))
H = int(input("Insira o numero de habitantes: "))
X = int(input("Insira o numero da cap. de transf. em zumbi: "))
Y = int(input("Insira o numero de zumbis que pode matar por dia: "))
i = 1
NZ = 0
while( H > 0):
	NZ =   (Z * X) - NZ
	
	H = H - NZ
	Z = Z + NZ - Y
	i = i + 1
print(i)