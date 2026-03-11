x= input("resposta de satisfação:")
a=0
while(x.upper() !='S'and (x.upper() !='SIM' or x.upper() !='NAO')):
	if(x.upper() =='SIM'):
		a=a+1
		x= input("resposta de satisfação:")
	if(x.upper() == 'NAO'):
		x= input("resposta de satisfação:")
print(a)