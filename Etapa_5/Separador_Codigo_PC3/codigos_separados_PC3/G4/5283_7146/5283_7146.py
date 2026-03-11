n = int(input(""))
i = 0
p = 0
while (n != 0):
	i = i + 1
	if (n > 0):
		p = p + 1
	n = int(input(""))	

total = (p / i) * 100
print(i)
print(round(total, 2))