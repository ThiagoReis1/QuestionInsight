

b1=input('Digite sim ou nao:').upper()

tos=0
ton=0
gh='S'
while(b1!=gh):
	if(b1=='SIM'):
		tos=tos+1
	if(b1=='NAO'):
		ton=ton+1
	b1=input('Digite sim ou nao:').upper()

k=tos+ton	
j=tos/k	
	
	
print(tos+ton)
print(round(j*100,2))