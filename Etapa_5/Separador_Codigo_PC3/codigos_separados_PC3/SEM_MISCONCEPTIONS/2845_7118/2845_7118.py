from numpy import*

senha = array(eval(input()))

a = [0, 9]

for a in range(size(senha)):
	if senha[a] == 9:
		senha[a] = 0
	else:
		senha[a] = senha[a] + 1
	

print(senha)