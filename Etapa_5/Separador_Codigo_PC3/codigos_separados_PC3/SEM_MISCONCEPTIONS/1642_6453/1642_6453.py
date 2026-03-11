from numpy import*
vetor=array(eval(input("Vetor: ")))
tam=size(vetor)
quant=0
for i in range(tam):
	if(vetor[i]%5==0):
		quant=quant+1
zeros=zeros(quant,dtype=int)
j=0
for i in range(tam):
	if(vetor[i]%5==0):
		zeros[j]=i
		j=j+1
print(quant)
print(zeros)
