from numpy import *
a = array(eval(input()))

p = 0
for i in a:
	if i == 1:
		p = p + 80
	if i == 2:
		p = p + 40
	if i == 3:
		p = p + 20
	if i == 4:
		p = p + 10
print(p)