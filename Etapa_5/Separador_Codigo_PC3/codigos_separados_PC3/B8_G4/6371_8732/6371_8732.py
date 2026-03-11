from numpy import * 
c = array(eval(input("Codigo: ")))
for i in range(size(c)):
	if c[i] == 0:
		c[i] = 9 ** 2
	elif c[i] == 1:
		c[i] = (1 - 1) ** 2
	elif c[i] == 2:
		c[i] = (2 - 1) ** 2
	elif c[i] == 3:
		c[i] = (3 - 1) ** 2
	elif c[i] == 4:
		c[i] = (4 - 1) ** 2
	elif c[i] == 5:
		c[i] = (5-1) ** 2
	elif c[i] == 6:
		c[i] = (6 - 1) ** 2
	elif c[i] == 7:
		c[i] = (7 - 1) ** 2
	elif c[i] == 8:
		c[i] = (8 - 1) ** 2
	elif c[i] == 9:
		c[i] = (9 - 1) ** 2
print(c)