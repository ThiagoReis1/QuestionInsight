from numpy import*
z = zeros(4, dtype = int)
c = input("EVAD: ").split(',')

for i in range(size(c)):
	if (c[i]=="E"):
		z[0] = z[0] + 1
	if (c[i]=="V"):
		z[1] = z[1] + 1
	if (c[i]=="A"):
		z[2] = z[2] + 1
	if (c[i]=="D"):
		z[3] = z[3] + 1
print(z)