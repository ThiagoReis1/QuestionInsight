from numpy import*

a=array(eval(input('Custo dos produtos:')))

n=0
sub=2.50



for i in range(size(a)):
	if(a[i]>40):
		n=n+1

ab=n*sub
bv=sum(a)
cn=bv-ab
		
print(round(cn,2))