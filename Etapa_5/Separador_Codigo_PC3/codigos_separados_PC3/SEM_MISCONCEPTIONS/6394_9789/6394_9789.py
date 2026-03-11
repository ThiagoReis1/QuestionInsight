from numpy import*
senha_nova = array(eval(input("")))

for i in range(size(senha_nova)):
	if senha_nova[i] == 9:
		senha_nova[i] = 0
	else:
		senha_nova[i] = senha_nova[i] + 1
		
print(senha_nova)
