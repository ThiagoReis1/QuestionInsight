from numpy import*
etq= (input('Digite o conteudo da etiqueta:')).upper()
i=0
vogal=0
consoante=0
while(i<size(etq)):
	if(etq[i]=='A' or etq[i]=='E'or etq[i]=='I'or etq[i]=='O'
		or etq[i]=='U'):
		vogal=vogal+1
		consoante= len(etq)-vogal
		i=i+1
#print(vogal)
#print(consoante)
print(round(vogal*0.15 + consoante*0.17,2))		
		
	
	
