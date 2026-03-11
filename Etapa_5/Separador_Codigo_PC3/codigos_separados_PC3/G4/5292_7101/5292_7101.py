c = input("Cor da casa: ").upper()
x = 0
y = 0
while (c != "S"):
	if (c == "PRETA"):
		x = x + 1
	y = y + 1
	c = input("Cor da casa: ").upper()
total = (x*100)/y
print(y)
print(round(total,2))