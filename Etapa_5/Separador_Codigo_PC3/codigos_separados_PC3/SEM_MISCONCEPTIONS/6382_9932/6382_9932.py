from numpy import*
senha = eval(input())

for i in range(len(senha)):
	if senha[i] == 0:
		senha[i] = 1
	elif senha[i] == 9:
		  senha[i] = 0
	else: 
		senha[i] = (senha[i] + 1)**2

senha = array(senha)
print(senha)