from numpy import *

num = array(eval(input("xxxx: ")))

for i in range(size(num)):
		num[i] = num[i] * 2
zeros(num, dtype=int)
print(num)