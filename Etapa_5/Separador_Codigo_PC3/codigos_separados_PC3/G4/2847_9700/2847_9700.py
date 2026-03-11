from numpy import*
cont=array(eval(input()))
for i in range(0,size(cont)):
	if cont [i] == 9:
		cont [i] = 0
	else:
		cont[i]=(cont[i])**2
	
print(cont)
