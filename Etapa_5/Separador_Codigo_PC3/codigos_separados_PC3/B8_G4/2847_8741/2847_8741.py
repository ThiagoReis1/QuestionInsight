from numpy import *

e = array(eval(input("vetor: ")))
for i in range(size(e)):
	if e[i] == 0:
		e[i] = 0 ** 2
	elif e[i] == 1:
		e[i] = 1 ** 2
	elif e[i] == 2:
		e[i] = 2 ** 2
	elif e[i] == 3:
		e[i] = 3 ** 2
	elif e[i] == 4:
		e[i] = 4 ** 2
	elif e[i] ==5:
		e[i] = 5 ** 2
	elif e[i] == 6:
		e[i] = 6 ** 2
	elif e[i] == 7:
		e[i] = 7 ** 2
	elif e[i] == 8:
		e[i] = 8 ** 2
	elif e[i] == 9:
		e[i] = 9 ** 2
print(e)


