from numpy import*

n = array(eval(input("")))

for i in range(size(n)):
	if n[i] == 0:
		n[i] = 9
	else:
		n[i] = n[i] - 1
print(n)