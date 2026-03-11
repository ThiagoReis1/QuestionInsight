a = input("Qual o nome do aminoacido?")
O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.0079

if(a.lower() == "aspartato"):
	peso = 4*C+H*6+N+4*O
	print(round(peso,2))
elif(a.lower() == "fenilalanina"):
	peso = 9*C+11*H+2*O+S
	print(round(peso,2))
elif(a.lower() == "tirosina"):
	peso = 9*C+11*H+N+3*O
	print(round(peso,2))
else:
	print("Entrada: ",a)
	print("Dado Invalido")


