from numpy import*
num = array(eval(input(":")))
senha = zeros(size(num), dtype = int)

for i in range (size(num)): 
	if num[i] == 0:
		senha[i] = num ** 2
	else:
		senha[i] = num[i] ** 2
	
print(senha)