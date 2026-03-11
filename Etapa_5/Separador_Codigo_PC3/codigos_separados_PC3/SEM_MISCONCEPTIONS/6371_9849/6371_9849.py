from numpy import *
senha = array(eval(input('insira a sua senha: ')))
senha_porta = zeros(size(senha), dtype=int)

for i in range(size(senha)):
	if senha [i] == 0:
		senha_porta[i] = 9**2
	else:
		senha_porta[i] = (senha[i] -1) ** 2

print(senha_porta)