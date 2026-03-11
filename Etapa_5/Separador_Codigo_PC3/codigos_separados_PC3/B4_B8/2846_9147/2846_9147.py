from numpy import *

senha = array(eval(input("insira sua senha numerica: ")))
senha_new = zeros(size(senha), dtype=int)

for i in range(size(senha)):
	if	senha[i] == 0:
		senha_new[i] = senha[i] * 2
	elif	senha[i] == 2:
		senha_new[i] = senha[i] * 2
	elif	senha[i] == 3:
		senha_new[i] = senha[i] * 2
	elif	senha[i] == 4:
		senha_new[i] = senha[i] * 2
	elif	senha[i] == 5:
		senha_new[i] = senha[i] * 2
	elif	senha[i] == 6:
		senha_new[i] = senha[i] * 2
	elif	senha[i] == 7:
		senha_new[i] = senha[i] * 2
	elif	senha[i] == 8:
		senha_new[i] = senha[i] * 2
	elif	senha[i] == 9:
		senha_new[i] = senha[i] * 2
	elif	senha[i] == 1:
		senha_new[i] = senha[i] * 2
		
print(senha_new)
 