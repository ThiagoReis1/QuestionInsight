from numpy import *
v = array(eval(input()))

cont = 0
for i in v:
	if i > 90:
		cont = cont + 1
print(round(sum(v) - cont * 6.50,2))
		