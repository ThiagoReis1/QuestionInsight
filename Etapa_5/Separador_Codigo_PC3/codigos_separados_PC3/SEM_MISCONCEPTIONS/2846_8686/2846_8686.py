from numpy import *

senha = array(eval(input()))
senha_alt = zeros(size(senha), dtype=int)

for i in range(size(senha)):
	if senha[i] != 0:
		senha_alt[i] = senha[i] * 2
	else:
		senha[i] = 0
print(senha_alt)		