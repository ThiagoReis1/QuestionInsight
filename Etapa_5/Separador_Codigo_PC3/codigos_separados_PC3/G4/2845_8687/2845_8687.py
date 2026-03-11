from numpy import *

num = array(eval(input()))
num1 = zeros(size(num), dtype=int)

for i in range(len(num)):
	if num[i] == 9:
		num1[i] = 0
	else:
		num1[i] = num[i] + 1
print(num1)
