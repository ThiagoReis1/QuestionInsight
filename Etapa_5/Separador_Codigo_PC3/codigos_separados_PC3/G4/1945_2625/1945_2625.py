nome = input(" ")
O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794
peso1 = 4*C + 6*H + N + O*4
peso2 = 3*C + 7*H + N + 2*O + S

if(nome.lower() == "aspartato"):
	print(round(peso1,2))

if(nome.lower() == "cisteina"):
	print(round(peso2,2))