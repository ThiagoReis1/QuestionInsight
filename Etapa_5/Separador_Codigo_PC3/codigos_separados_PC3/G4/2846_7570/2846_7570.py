from numpy import*
x = array(eval(input(" ")))
i = 0

for i in range(size(x)):
	x[i] = 2 * x[i]
print(x)