from numpy import*
n = array(eval(input()))
for i in range(size(n)):
	if(n[i] > 0):
		n[i] = (n[i] - 1)**3
	else:
		n[i] = 729
print(n)