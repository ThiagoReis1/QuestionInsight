nome = input()

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

if(nome.lower() == "aspartato"):
	a = ((4*C) + (6*H) + (N) + (4 * O))
	print(round(a,2))
	
else:
	c = ((3*C)+ (7*H)+ (N) + (2*O) + (S))
	print(round(c,2))
	