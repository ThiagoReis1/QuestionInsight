from numpy import*

v = array(eval(input(": ")))
x = size(v)
total = 0

for i in range(x):
	if v[i] > 80.00:
		total = total + (v[i] - 15/100*v[i])
	else:
		total = total + v[i]
print(round(total,2))