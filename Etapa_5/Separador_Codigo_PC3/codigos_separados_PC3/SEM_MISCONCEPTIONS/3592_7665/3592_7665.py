from numpy import*

vetor = array(eval(input()))
tot=100
i=0
tamanho = size(vetor)

while i < tamanho :
	if(vetor[i]==1):
		tot=tot/1
	if(vetor[i]==2):
		tot=tot*2
	if(vetor[i]==3):
		tot=tot/3
	if(vetor[i]==4):
		tot=tot*4
	if(vetor[i]==5):
		tot=tot/5
	if(vetor[i]==6):
		tot=tot*6
	i=i+1
print(round(tot, 2))
