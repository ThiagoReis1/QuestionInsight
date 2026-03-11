from numpy import*
mens = array(eval(input()))
for i in range(0,size(mens)):
	if mens[i] == 0:
		mens[i] = 9 ** 3
	else:
		mens[i] = (mens[i] - 1)**3
print(mens)