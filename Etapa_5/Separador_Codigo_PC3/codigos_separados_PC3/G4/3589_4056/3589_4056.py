from numpy import *
x = array (eval(input("digite: ")))
p = 0
i = 0

while i < size(x):
	if x[i] == 1:
		p = p + 80
	if x[i] == 2:
		p = p + 40
	if x[i] == 3:
		p = p + 20
	if x[i] == 4:
		p = p + 10
	i += 1
print(round(p,2))