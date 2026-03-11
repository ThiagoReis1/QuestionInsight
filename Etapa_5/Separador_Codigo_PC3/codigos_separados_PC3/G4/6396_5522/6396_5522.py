from numpy import*

n = array(eval(input()))
for i in range(0, size(n)):
	if n[i] == 7:
		n[i] =14
	else:
		n[i]=n[i]*2
print(n)