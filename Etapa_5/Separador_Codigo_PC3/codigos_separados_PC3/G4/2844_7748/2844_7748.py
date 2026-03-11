from numpy import*

cod= array(eval(input('cod:')))

for i in range(size(cod)):
	if(cod[i]!=0):
		cod[i] = cod[i]-1
		
	else:
		cod[i]=9
print(cod)
		
	