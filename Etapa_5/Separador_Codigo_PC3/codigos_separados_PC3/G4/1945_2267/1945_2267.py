amino = input("digite o aminoacido aspartato ou cisteina: ")
O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

if(amino.lower() == "aspartato"):
	x = (4*C)+(6*H)+(1*N)+(4*O)

else:
	x = (3*C)+(7*H)+(1*N)+(2*O)+(1*S)

print(round(x, 2))