from numpy import*

senha = array(eval(input('')))


for i in range(size(senha)):
	if senha[i]==0:
		senha[i]=9**2
	else:
		senha[i] = (senha[i]-1)**2
print(senha)