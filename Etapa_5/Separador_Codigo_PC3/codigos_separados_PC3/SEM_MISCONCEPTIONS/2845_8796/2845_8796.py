from numpy import *

senha = array(eval(input()))

senha_alt = zeros(size(senha), dtype=int)

for i in range(size(senha)):
	if senha[i] == 9:
		senha_alt[i] = 0
	else:
		senha_alt[i] = senha[i] + 1
print(senha_alt)