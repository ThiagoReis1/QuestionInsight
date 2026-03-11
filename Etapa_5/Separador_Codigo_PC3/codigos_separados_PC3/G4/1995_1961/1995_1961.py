nome=input("Nome do aminoacido:").lower()

O=15.9994
C=12.011
N=14.0067
S=32.066
H=1.00794

if(nome == "aspartato"):
	A=(C*4+H*6+N+O*4)
	print(round(A,2))
elif(nome == "cisteina" ):
	C=(C*3+H*7+N+O*2+S)
	print(round(C,2))
elif(nome == "metionina"):
	M=(C*5+H*11+N+O*2+S)
	print(round(M,2))
else:
	print("Entrada: %s" %(nome))
	print("Dado Invalido")