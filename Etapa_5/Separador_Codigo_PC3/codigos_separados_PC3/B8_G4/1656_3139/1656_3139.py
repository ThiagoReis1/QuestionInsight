from numpy import*
from numpy.linalg import*

x = input("string: ").upper()
x = x.split(',')

cont = zeros(5,dtype = int)
i = 0

while(i < len(x)):
	if(x[i] == 'BE'):
		cont[0] = cont[0] + 1
	elif(x[i] == 'ES'):
		cont[1] = cont[1] + 1
	elif(x[i] == 'FR'):
		cont[2] = cont[2] + 1
	elif(x[i] == 'IT'):
		cont[3] = cont[3] + 1
	elif(x[i] == 'PT'):
		cont[4] = cont[4] + 1
		
print(cont[i])
print(cont)
