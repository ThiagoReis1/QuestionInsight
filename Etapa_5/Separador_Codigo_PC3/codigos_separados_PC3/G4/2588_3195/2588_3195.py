from numpy import *
reg = array(eval(input("")))
cont = 0
for i in range(0, size(reg)):
	if(i != 0):
		if(reg[i] > (0.2 * reg[0] + reg[0]) and reg[i] < (0.5 * reg[0] + reg[0])):
			print(i)
			cont += 1
print(cont)