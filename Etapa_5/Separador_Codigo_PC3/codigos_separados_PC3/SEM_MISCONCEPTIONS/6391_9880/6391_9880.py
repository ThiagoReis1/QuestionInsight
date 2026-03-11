from numpy import *

senha = array(eval(input("Insira a senha: ")))
senha_nova = zeros(size(senha), dtype=int)
						 
for i in range(size(senha)):
	if senha[i] == 0:
		senha_nova[i] = 9 ** 3
	else:
		senha_nova[i] = (senha[i] - 1) ** 3
				
print(senha_nova, end="")