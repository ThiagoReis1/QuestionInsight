from numpy import *

vet = array(eval(input))
cresc = zeros(size(vet), dtype = int)

x = 0
for i in vet:
	if(i < i + 1):
		cresc[x] = 