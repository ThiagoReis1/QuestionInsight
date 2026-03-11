from numpy import*
senha = array(eval(input('insira a sua senha: ')))
senha_new = zeros(size(senha), dtype=int)

for i in range(size(senha)):
	if senha[i] == 0:
		senha_new[i] = 9**3
	else:
		senha_new[i] = (senha[i]-1)**3
		
print(senha_new)