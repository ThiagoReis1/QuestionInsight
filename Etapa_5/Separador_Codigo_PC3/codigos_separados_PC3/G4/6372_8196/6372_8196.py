from numpy import*
var1 = input(": ").split(",")
cont = zeros(4, dtype = int)
for i in var1:
	if(i == 'A'):
		cont[0] = cont[0] + 1
	if(i == 'B'):
		cont[1] = cont[1] + 1
	if(i == 'L'):
		cont[2] = cont[2] + 1
	if(i == 'H'):
		cont[3] = cont[3] + 1
print(cont)
	