from numpy import *
x = array(eval(input("dados ")))
p = 0
for i in x:
	if i == 1 or i == 6:
		p = p + 10
	if i == 2 or i == 4:
		p = p + 5
	if i == 3:
		p = p
	if i == 5:
		p = p + 20
print(p)