from numpy import*

ra = array(eval(input(": ")))

for i in range(size(ra)):
	if ra[i] == 0:
		ra[i] = 9
	else:
		ra [i] = ra[i] - 1
print(ra)
