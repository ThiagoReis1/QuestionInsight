N=int(input("posicao:"))
soma=0
while(N!=0):
	if(N==1):
		soma=soma+25
	elif(N==2):
		soma=soma+18
	elif(N==3):
		soma=soma+12
	elif(N>=4 and N<=10):
		soma=soma+(14-N)
	N=int(input("posicao"))
print(soma)
