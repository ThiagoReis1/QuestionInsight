from numpy import*
x = input()
v = x.split(',')
y = zeros (5,dtype=int)
a = 0
for i in v:
	if (i == "AR"):
		y[0] = y[0] + 1
	if (i == "BR"):
		y[1] = y[1] + 1
	if (i == "CL"):
		y[2] = y[2] + 1
	if (i == "CO"):
		y[3] = y[3] + 1
	if (i == "UY"):
		y[4] = y[4] + 1
print(max(y))		
print(y)		