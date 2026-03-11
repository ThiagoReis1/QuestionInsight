from numpy import *
senha = array(eval(input("insira uma senha: ")))
senha_nova = zeros(size(senha), dtype=int)

for i in range(size(senha)):
	if senha[i] == 9:
		senha_nova[i] = 0
	else:
		senha_nova[i] = senha[i] + 1
print(senha_nova)