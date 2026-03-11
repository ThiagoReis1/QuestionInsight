from numpy import*

saques= array(eval(input('insira:')))
v1=0

for i in range(size(saques)):
	if saques[i] <= 50:
		v1 += 1 
	
ind=zeros(v1,dtype=int)
print(v1)
v=0 

for i in range(size(saques)):
	if saques[i] <= 50:
		ind[v]= i
		v += 1
print(ind)
