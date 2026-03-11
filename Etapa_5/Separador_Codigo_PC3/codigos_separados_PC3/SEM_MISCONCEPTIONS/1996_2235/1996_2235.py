a = input("nome do aminoacido: ").lower()


O=15.9994
C=12.011
N=14.0067
S=32.066
H=1.0079


if(a =="FENILALANINA"):
	a = C*9+H*11+O*2+S
	print(round(a,2))
elif (x == "ASPARTATO"):
	x = C*4+H*6+N+O*4
	print(round(x,2))
elif (y == "TIROSINA"):
   y = C*9+H*11+N+O*3
	print(round(y,2))
	
else:
	print("entrada:",a)
	print("Dado Invalido")
	

	
	
	