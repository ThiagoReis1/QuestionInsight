from numpy import*
x = input().split(',')
cont = zeros(5, dtype=int)
for i in range(size(x)):
	if(x[i] ==  'P'):
		cont[0] = cont[0] + 1
	elif(x[i] == 'C'):
		cont[1] = cont[1] + 1
	elif(x[i] == 'M'):
		cont[2] = cont[2] + 1
	elif(x[i] == 'V'):
		cont[3] = cont[3] + 1 
	else:
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)
		
	
	
