from numpy import*
vetor = array(eval(input()))


quati=0
i=0
j=0
while(i<size(vetor)):
	if(vetor[i]%5==0):
		quati = quati+1
	i=i+1
lolcura=zeros(quati,int)
i=0
while(i<size(vetor)):
	if(vetor[i]%5==0):
		lolcura[j]=int(i)
		j=j+1
	i=i+1

print(quati)
print(lolcura)

