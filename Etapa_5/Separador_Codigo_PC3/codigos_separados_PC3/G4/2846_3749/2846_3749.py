from numpy import *

num = array(eval(input("numeros: ")))


i = 0

for i in range(size(num)):
	num[i] = num[i] * 2
	
print(num)