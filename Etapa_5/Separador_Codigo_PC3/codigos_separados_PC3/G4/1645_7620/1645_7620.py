from numpy import*

a=array(eval(input('Digite o vetor:')))

ma=0



for i in range(size(a)):
	if(a[i]>=2000):
		ma=ma+1

		
vet=zeros(ma,dtype=int)
j=0
for i in range(size(a)):
	if(a[i]>=2000):
		vet[j]=i
		j=j+1
	
		
print(ma)
print(vet)
