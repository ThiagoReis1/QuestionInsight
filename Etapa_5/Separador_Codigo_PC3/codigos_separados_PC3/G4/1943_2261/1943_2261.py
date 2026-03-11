#aminoacido
amino = input("digite o aminoácido isoleucina ou metionina  :")

#moleculas
O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

if(amino.lower() == "isoleucina"):
	x = (6*C)+(13*H)+(1*N)+(2*O)
else:
	x = (5*C)+(11*H)+(N*1)+(O*2)+(S*1)

print(round(x, 2))
