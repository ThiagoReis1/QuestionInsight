from numpy import*

cont = input("Diga: ").upper().split(',')

v = zeros(4, dtype = int)


for i in range(size(cont)):
	
	if (cont[i] == 'C'):
		v[0] = v[0] + 1
		
	if (cont[i] == 'D'):
		v[1] = v[1] + 1
		
	if (cont[i] == 'V'):
		v[2] = v[2] + 1
		
	if (cont[i] == 'U'):
		v[3] = v[3] + 1
		
print(v)
		

