from numpy import *

senha = array(eval(input("Digite sua senha: ")))

for i in range(size(senha)):
	if senha[i] == 9:
		senha[i] = -1
	senha[i] = (senha[i] + 1) ** 2 
	
print(senha)
	