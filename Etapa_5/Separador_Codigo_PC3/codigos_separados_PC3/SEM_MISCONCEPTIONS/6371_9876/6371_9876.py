from numpy import *

senha = array(eval(input()))
nova = zeros(size(senha), dtype=int)
for i in range(size(senha)):
	if senha[i] == 0:
		nova[i] = 9**2
		
	else:
		nova[i] = (senha[i] -1)**2
print(nova)
		