var = input().upper()
i = 0
total = 0

while i < len(var):
	if var[i] == "I":
		total += 3.75
	elif var[i] == "M":
		total += 4.50
	elif var[i] == "S":
		total += 2.90
	i += 1
print(round(total, 2))






