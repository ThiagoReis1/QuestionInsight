from numpy import*
v = array(eval(input("digite: ")))

c = 0

for i in range(size(v)):
	if (v[i] < v[0]) and (i != 0) and (v[i] != 0):
		print(i)
		c = c + 1
print(c)


