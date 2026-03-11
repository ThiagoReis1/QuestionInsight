from numpy import*

v = input("a: ").split(',')

c = zeros(5, dtype=int)

for x in v:
	if(x == "P"):
		c[0] = c[0] + 1
	elif(x == "C"):
		c[1] = c[1] + 1
	elif(x == "R"):
		c[2] = c[2] + 1
	elif(x == "L"):
		c[3] = c[3] + 1
	elif(x == "B"):
		c[4] = c[4] + 1
print(max(c))
print(c)	

