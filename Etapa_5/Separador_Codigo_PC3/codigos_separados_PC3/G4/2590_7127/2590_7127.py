from numpy import *

v = array(eval(input("Digite os valores: ")))

b = 0

for i in range(size(v)):
	if(i != 0):
		if(v[0] > v[i]):
			b = b + 1
			print(i)
print(b)
		
