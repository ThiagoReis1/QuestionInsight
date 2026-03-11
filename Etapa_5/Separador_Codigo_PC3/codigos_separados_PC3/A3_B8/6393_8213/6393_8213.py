from numpy import*
vetor=array(eval(input(">>>>>>")))
r=zeros(size(vetor),dtype=int)
for i in range(size(vetor)):
	if vetor[i]!=9:
		vetor[i]=vetor[i]+1
		r=vetor**3
	elif vetor[i]==9:
		vetor[i]=vetor[i]*0
		r=vetor**3
print(r)