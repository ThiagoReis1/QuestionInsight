from numpy import*

v = array(eval(input('insira o custo dos itens:')))

total = 0

for i in v:
	if i > 160:
		total = total + i - 25
	else:
		total = total + i
	
print(total)

