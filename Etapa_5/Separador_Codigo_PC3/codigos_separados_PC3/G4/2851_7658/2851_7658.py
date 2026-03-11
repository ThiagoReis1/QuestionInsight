from numpy import *
vet= array(eval(input('valores:')))
SOMA= 0
for i in vet:
	if i != 99:
		SOMA= SOMA + i
	else:
		SOMA= SOMA*2
print(SOMA)