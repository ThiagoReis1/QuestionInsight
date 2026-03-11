from numpy import *

a = array(eval(input("a: ")))
p = 10000

for i in a:
	if i == 1:
		p = p * 2
	elif i == 2:
		p = p
	elif i == 3:
		p = p/2
	elif i == 4:
		p = p/4
print(p)