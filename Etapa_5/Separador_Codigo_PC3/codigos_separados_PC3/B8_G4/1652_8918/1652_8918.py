from numpy import*
e = input("etnia: ").upper()
e = e.split(",")
c = zeros(5, dtype = int)

for i in e:
	if i == "B":
		c[0] += 1
	elif i == "PA":
		c[1] += 1
	elif i == "PR":
		c[2] += 1
	elif i == "A":
		c[3] += 1
	elif i == "I":
		c[4] += 1
print(max(c))
print(c)