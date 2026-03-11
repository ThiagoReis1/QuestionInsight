x = input("").upper()
y = 0

for i in range(len(x)):
	if x[i] == "E":
		y = y + 1
		
print(y)