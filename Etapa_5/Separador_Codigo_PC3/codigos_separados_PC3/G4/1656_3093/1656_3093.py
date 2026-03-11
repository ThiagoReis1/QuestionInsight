from numpy import*
x = input()
z = x.split(',')
a = 0
y = zeros(5,dtype=int)
for i in z:
	if (i == "BE"):
		y[0] = y[0] + 1
		a = a + 1
	if (i == "ES"):
		y[1] = y[1] + 1
		a = a + 1
	if (i == "FR"):
		y[2] = y[2] + 1
		a = a + 1
	if (i == "IT"):
		y[3] = y[3] + 1
		a = a + 1
	if (i == "PT"):
		y[4] = y[4] + 1
		a = a + 1
print(max(y))
print(y)