import numpy as np
string=input()
lista=string.split(',')

saida=np.array([0,0,0,0,0,0])

for x in lista:
	if(x=="MC"):
		saida[0]+=1
	if(x=="C"):
		saida[1]+=1
	if(x=="CM"):
		saida[2]+=1
	if(x=="EM"):
		saida[3]+=1
	if(x=="E"):
		saida[4]+=1
	if(x=="ME"):
		saida[5]+=1

print(saida.max())
print(saida)