from numpy import *

num = array(eval(input(": ")))
final = zeros(size(num), dtype=int)

for i in range(size(num)):
	if num[i] != 0:
		final[i] = num[i] - 1
	elif num[i] == 0:
		final[i] = 9
		
print(final)	
	


