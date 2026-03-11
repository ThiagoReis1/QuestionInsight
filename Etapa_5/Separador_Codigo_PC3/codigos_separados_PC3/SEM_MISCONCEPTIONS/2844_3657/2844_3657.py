from numpy import*
mensagem=array(eval(input("De o vetor mensagem: ")))
n=size(mensagem)
i=0
vetor=zeros(n,dtype=int)
while(i<n):
	if(mensagem[i]>0):
		vetor[i]=mensagem[i]-1
	else:
		vetor[i]=9
	i=i+1
print(vetor)
		