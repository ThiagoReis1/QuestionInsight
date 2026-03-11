from numpy import*

e = array(eval(input("codigo: ")))

for i in range(size(e)):
	if e[i] == 0:
		e[i] = 9 ** 2
	elif e[i] == 1:
		e[i] = (1 -1) ** 2
	elif e[i] == 2:
		e[i] = (2 - 1) ** 2
	elif e[i] == 3:
		e[i] = (3-1) ** 2
	elif e[i] == 4:
		e[i] = (4 - 1) ** 2
	elif e[i] == 5:
		e[i] = (5-1) ** 2
	elif e[i] == 6:
		e[i] = (6-1) ** 2
	elif e[i] == 7:
		e[i] = (7-1) ** 2
	elif e[i] == 8:
		e[i] = (8-1) ** 2
	elif e[i] == 9:
		e[i]  = (9-1) ** 2
print(e)
