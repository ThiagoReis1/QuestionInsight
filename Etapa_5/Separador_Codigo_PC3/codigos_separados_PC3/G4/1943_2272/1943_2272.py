aminoacido = input("aminoacido:")
O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00764

if(aminoacido=="isoleucina"):
	mensagem = 6*C+13*H+1*N+2*O
else:
	mensagem = 5*C+11*H+1*N+2*O+1*S

print(round(mensagem,2))

