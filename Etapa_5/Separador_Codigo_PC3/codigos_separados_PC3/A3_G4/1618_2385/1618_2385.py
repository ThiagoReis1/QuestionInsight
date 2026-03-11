from numpy import*
vet=array(eval(input()))
saida=""
i=0
x=0


while(i<size(vet)):
	
	
	if(i+1==size(vet)):
		saida=saida+str(vet[i])
	elif(size(vet)-i-1==1):
		saida=saida+str(vet[i])+"x"+" + "
	else:
		saida=saida+str(vet[i])+"x^"+str(size(vet)-1-i)+" + "

	
	i=i+1
	
print(saida)

	
	
	