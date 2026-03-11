amino=input("Digite o nome do aminoácido: ")
#Cisteina=input("Digite o nome do aminoácido")


O=15.9994
C=12.011
N=14.0067
E=32.066
H=1.00794

valor=(C*4+H*6+N+O*4)
valor2=(C*3+H*7+N+O*2+S)



if(amino.lower()=="aspartato"):
	
	print(round(valor,2))
	
else:	
	print(round(valor2,2))
	

