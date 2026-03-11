from numpy import *

x = array(eval(input("aneis: ")))
p = 0 
i = 0
while i < size(x):
	if x[i] == 1:
		p = p + 80
	elif x[i] == 2:
		p = p + 40
	elif x[i] == 3:
		p = p + 20
	elif x[i] == 4:
		p = p + 10
	i = i + 1

print(round(p, 2))