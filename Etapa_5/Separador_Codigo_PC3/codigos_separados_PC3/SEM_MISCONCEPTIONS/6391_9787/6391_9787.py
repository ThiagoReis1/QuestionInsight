from numpy import*

codigo = array(eval(input("")))


for i in range(size(codigo)):
	if codigo[i] == 0:
		codigo[i] = 9**3
	else:
		codigo[i] = (codigo[i]-1)**3
		
print(codigo)
		