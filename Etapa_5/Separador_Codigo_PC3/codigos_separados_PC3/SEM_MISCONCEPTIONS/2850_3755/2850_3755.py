from numpy import *
v=array(eval(input('Quais foram as vendas:')))
i=0
total=0
while i<size(v):
	if i>=0:
		total=total + v[i]
		i=i+1
	if total>55:
		total=0
print(total)
		