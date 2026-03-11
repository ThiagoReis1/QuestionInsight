from numpy import*
c = array(eval(input()))

total = 0

for i in range(size(c)):
	c[i] = c[i] + 1
	total = total + 1
	if(total >= 55):
		total = 0
	total = total + 1
print(total)

