A= input("nome do aminoacido: ")
O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

a =((C*4)+(H*6)+(N)+(O*4))
c =((C*3)+(H*7)+(N)+(O*2)+(S))

if (A.lower()=="aspartato"):
	print(round(a,2))
else:
	print(round(c,2))