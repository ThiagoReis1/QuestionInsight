from numpy import *

cod = array(eval(input()))
pss = zeros(size(cod), dtype = int)

for i in range (size(cod)):
	pss[i] = cod[i] ** 2
print(pss)