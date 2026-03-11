from numpy import*
v = input("Digite as cores: ").split(',')

c = zeros(5, dtype = int)

for i in range(size(v)):
	if v[i] == "P":
		c[0] = c[0]+1
	elif v[i] == "C":
		c[1] = c[1]+1
	elif v[i] == "M":
		c[2] = c[2] + 1
	elif v[i] == "V":
		c[3] = c[3]+1
	elif v[i] == "A":
	   c[4] = c[4] +1
print(max(c))
print(c)
	
	
	