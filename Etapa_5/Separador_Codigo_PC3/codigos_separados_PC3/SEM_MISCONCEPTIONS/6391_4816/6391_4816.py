from numpy import *

senha = array(eval(input()))
nova_senha = zeros(size(senha), dtype=int)


for i in range(size(senha)):
	if senha[i] == 0:
		nova_senha[i] = 9**3
	else:
		nova_senha[i] = (senha[i] - 1) ** 3
print(nova_senha)