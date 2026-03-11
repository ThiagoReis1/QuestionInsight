from numpy import * 
x = input("Cor: ").upper()
y = x.split(',')
z= zeros(5, dtype=int)
for i in range(size(y)): 
	if y[i] == 'P':
		z[0] = z[0] + 1
	elif y[i] == 'C':
		z[1] = z[1] + 1
	elif y[i] == 'R':
		z[2] = z[2] + 1
	elif y[i] == 'L':
		z[3] = z[3] + 1
	else:
		z[4] = z[4] + 1
print(max(z))
print(z)
