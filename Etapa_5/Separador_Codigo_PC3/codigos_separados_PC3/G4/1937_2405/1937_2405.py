aminoacido=input()
					  	
O=15.9994
C=12.011
N=14.00674
H=1.00794
					  
va=C*5+H*11+N+O*2
an=C*3+H*7+N+O*2
					  
if(aminoacido.upper()=="ALANINA"):
	print(round(an, 2))
			
if(aminoacido.upper()=="VALINA"):
	print(round(va, 2))

		