from numpy import *
senha=array(eval(input()))
for i in range(0,size(senha)):
	if senha[i] == 0:
		senha[i]= 9**3
	else:
		senha[i]=(senha[i]-1)**3
print(senha)
    