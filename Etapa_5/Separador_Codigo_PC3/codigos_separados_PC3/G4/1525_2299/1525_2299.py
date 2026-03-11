vl = int(input(""))
va = int(input(""))
ve = int(input(""))

t = 0

while (vl > 1000):
	vl = vl + va - ve
	t = t + 1
	
print(t)