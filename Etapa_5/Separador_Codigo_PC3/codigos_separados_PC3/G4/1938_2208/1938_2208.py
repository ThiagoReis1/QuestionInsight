amin=input("Digite o valor do aminoacido (ARGININA/TIROSINA): ")
O=15.9994
C=12.011
N=14.00674
H=1.00794

if(amin.upper()=="ARGININA"):
	A=(C*6+H*15+N*4+O*2)
	print(round(A,2))
else:
	T=(C*9+H*11+N*1+O*3)
	print(round(T,2))