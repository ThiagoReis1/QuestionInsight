num=int(input("numero sorteado: "))

nm5=0
cont=0

while(num<=10):
	cont=cont+1
	if(num==-1):
		nm5=nm5+1
		porcent=(nm5*100)/cont-1
		print(cont-1)
		print(round(porcent,2))
	
	num=int(input("numero sorteado: "))
		