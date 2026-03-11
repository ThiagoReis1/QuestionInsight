from numpy import *

ent = array(eval(input("")))

cont = 0
x = sum(ent)

while size(ent) > cont:
	if ent[cont] > 40:
		x = x - 2.5
	else:
		x = x
	cont += 1
print(round(x,2))	