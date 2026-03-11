from numpy import*

c = input(" ").split(",")
x = zeros(4, dtype = int)

for i in c:
	if i == "E":
		x[0] += 1
	elif i == "V":
		x[1] += 1
	elif i == "A":
		x[2] += 1
	elif i == "D":
		x[3] += 1
print(x)