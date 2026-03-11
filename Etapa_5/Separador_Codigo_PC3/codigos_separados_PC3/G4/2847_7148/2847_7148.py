from numpy import*

d = array(eval(input()))
h = 0

for i in range(size(d)):
	if(d[i] >= 0 and d[i] <= 9):
		d[i] = d[i] ** 2
	h = h + 1
print(d)