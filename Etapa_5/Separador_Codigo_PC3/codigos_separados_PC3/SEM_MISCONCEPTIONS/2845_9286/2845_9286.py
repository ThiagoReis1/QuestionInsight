from numpy import *
senha = array(eval(input("Senha:")))
nova = zeros(size(senha), dtype=int)

for i in range(size(nova)):
	if senha[i] == 9:
		nova[i] = 0
	else:
		nova[i] = senha[i] + 1
		
print(nova)