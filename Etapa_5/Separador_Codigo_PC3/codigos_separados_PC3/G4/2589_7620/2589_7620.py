from numpy import*

a=array(eval(input('Digite o vetor:')))

n=0

for i in range(1,size(a)):
	if(a[i]>=a[0]):
		n=n+1
		print(i)
	
print(n)