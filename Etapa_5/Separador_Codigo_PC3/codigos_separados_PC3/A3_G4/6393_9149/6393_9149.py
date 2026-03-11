from numpy import *

n = array(eval(input('')))
num = zeros(size(n), dtype = int)
cont = 0

for i in range(size (n)):
	if n[i] == 9:
		num[i] == 0
	else:
		num[i] = (n[i]+1)**3
print(num)