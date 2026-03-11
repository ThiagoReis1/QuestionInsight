from numpy import*

x = input("String: ")
i = 0

M = 7.25
P = 4.75
R = 3.50
t = 0
c = 0

while (i < len(x)):
	if (x[i] == "M"):
		c += 1
		t += M
	elif (x[i] == "P"):
		t += P
		c += 1
	elif (x[i] == "R"):
		t += R
		c += 1
	i += 1

print(round(t,2))