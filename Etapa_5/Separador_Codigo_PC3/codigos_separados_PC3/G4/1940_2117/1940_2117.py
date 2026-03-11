amin=input("qual o aminoácido? ")

O=float(15.9994)
C=float(12.011)
N=float(14.0067)
H=float(1.00794)

if(amin.upper()=='GLUTAMINA'):
	g=(C*5+H*8+N*1+O*4)
	print(round(g,2))
	
else:
	t=(C*4+H*9+N+O*3)
	print(round(t,2))