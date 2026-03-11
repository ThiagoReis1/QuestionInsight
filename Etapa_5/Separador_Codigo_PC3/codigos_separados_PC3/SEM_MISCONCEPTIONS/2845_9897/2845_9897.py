from numpy import *

senha = array(eval(input('senha: ')))
senha_nv = zeros(size(senha), dtype=int)

for i in range(size(senha)):
	if senha[i] == 9:
		senha_nv[i] = 0
	else:
		senha_nv[i] = senha[i] + 1
print(senha_nv)
		