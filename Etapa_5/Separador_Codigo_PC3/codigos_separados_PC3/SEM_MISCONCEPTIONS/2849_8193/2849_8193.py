from numpy import*

v = array(eval(input("")))
total = 0
for i in range(size(v)):
	total = total + v[i]
	if (v[i] == 0):
		total = 0

print(total)
