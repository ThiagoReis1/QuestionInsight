from numpy import*

a = input("digite: ").upper().split(',')
c = zeros(4, dtype=int)

for i in range(len(a)):
	if(a[i] == 'A'):
		c[0] = c[0] + 1
	elif(a[i] == 'P'):
		c[1] =c[1] + 1
	elif(a[i] == 'D'):
		c[2] = c[2] + 1
	elif(a[i] == 'M'):
		c[3] = c[3] + 1

print(c)