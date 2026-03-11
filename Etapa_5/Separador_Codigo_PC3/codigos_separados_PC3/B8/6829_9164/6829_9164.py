prod= input().upper()
i = 0
total = 0
while i < len(prod):
	if prod[i] == "A":
		total += 19.90
	elif prod[i] == "L":
		total += 3.50
	elif prod[i] == "P":
		total += 4.25
	i += 1

print(round(total, 2))
