aminoacido = input("Informe o nome do aminoácido (aspartato ou cisteina): ")


O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

if(aminoacido.lower() == "aspartato"):
	amino = (C*4+H*6+N+O*4)

else:
	amino = (C*3+H*7+N+O*2+S)
	
print(round(amino,2))