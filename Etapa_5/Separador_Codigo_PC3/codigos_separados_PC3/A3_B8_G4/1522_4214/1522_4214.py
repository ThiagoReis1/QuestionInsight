qi=int(input("Quantidade inicial:"))
dm=int(input("Despesa mensal:"))
qm=int(input("Quantidade de moedas mensais:"))
qr=int(input("Quantidade roubada mensal:"))

pos= qm+qm
fin= dm+qr
res=pos-fin
while(res>=0):
	res=res-fin
	if(res>0):
		res=res-fin
		
	elif(res==0):
		print("acabou")
	