from numpy import*
x = input("x: ").upper().split(",")
z = zeros(5,dtype=int)

for i in range(size(x)):
	if x[i] == 'A':
		z[0] = z[0] + 1
	elif x[i] == 'B':
		z[1] = z[1] + 1
	elif x[i] == 'C':
		z[2] = z[2] + 1
	elif x[i] == 'D':
		z[3] = z[3] + 1
	else:
		z[4] = z[4] + 1

print(z)