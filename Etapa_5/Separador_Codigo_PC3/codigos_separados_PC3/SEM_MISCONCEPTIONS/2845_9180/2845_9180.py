from numpy import*

senha = array(eval(input('Digite a senha:')))

for i in range(size(senha)):
	if senha[i] == 9:
		senha[i] = 0
	else:	
		senha[i] = senha[i] + 1
		
print(senha)		
	