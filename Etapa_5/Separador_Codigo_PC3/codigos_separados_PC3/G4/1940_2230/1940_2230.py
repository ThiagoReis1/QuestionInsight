a = input("nome do aminoacido: ")
O = 15.9994
C = 12.011
N = 14.0067
H = 1.00794

if(a == "glutamina".upper()):
	peso = (C*5)+(H*8)+(N*1)+(O*4)
else:
	peso = (C*4)+(H*9)+(N+O*3)
print(round(peso,2))