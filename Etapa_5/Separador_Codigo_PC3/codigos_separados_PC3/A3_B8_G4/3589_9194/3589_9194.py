from numpy import*
v= array(eval(input('inserir vetor:')))
i=0
c=0

a= [1,2,3,4]

while i<size(v):
	if v[i]==1:
		c+=80
	elif v[i]==2:
		c+=40
	elif v[i]==3:
		c+=20
	elif v[i]==4:
		c+=10
	i+=1
	
print(c)
	