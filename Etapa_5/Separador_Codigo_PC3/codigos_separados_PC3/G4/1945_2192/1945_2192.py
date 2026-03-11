aminoacido = input()

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

if(aminoacido == "aspartato"):
	peso = round(float(C*4 + H*6 + N + O*4 ), 2)
	print(peso)
else:
	peso = round(float(C*3 + H*7 + N + O*2 + S), 2)
	print(peso)