from numpy import*
vetor=array(eval(input("vetor entrada e saida: ")))
i=0
n=size(vetor)
p=0
soma=0


while(i<n):
	soma=soma+vetor[i]
	i=i+1
	if(soma>=75):
		soma=75
	else:
		soma=soma
print(soma)







	
		
		
		
		
		