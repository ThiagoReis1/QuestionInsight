from numpy import*

saques = array(eval(input('insira:')))
s =0

for i in range(size(saques)):
	if saques[i] <= 50:
		s +=1
		
ind = zeros(s, dtype=int)
print(s)
m= 0
for i in range(size(saques)):
	if saques[i] <= 50:
		ind[m]=i
		m+=1
		
print(ind)