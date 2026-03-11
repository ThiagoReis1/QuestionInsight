from numpy import *

ver = array(eval(input()))

i = 0
soma = 0

while i < size(ver):
	
	if ver[i] == 10:
		soma = 10 * soma
		
	else:
		soma += ver[i]
	
	i += 1
		
print(soma)