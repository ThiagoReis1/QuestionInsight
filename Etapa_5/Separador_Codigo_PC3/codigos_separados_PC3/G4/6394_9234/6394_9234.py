from numpy import*
b = array(eval(input(" ")))

for i in range(size(b)):
	if (b[i] == 9):
		 b[i] = 0
	else:
		b[i] += 1
print(b)
		