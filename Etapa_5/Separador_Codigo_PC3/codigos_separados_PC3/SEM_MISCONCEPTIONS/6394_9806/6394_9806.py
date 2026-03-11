from numpy import *

senha = array(eval(input("Digite a senha: ")))
senha_new = zeros(size(senha), dtype = int)

for i in range(size(senha)):
	if senha[i] == 9:
		senha_new[i] = 0 
	else:
		senha_new[i] = senha[i] + 1
print(senha_new)
	
	