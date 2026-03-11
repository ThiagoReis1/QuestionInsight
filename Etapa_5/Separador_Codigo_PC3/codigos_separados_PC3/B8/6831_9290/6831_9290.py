s = input("s: ")
total = 0
for x in s:
	if x == "A":
		total += 16.75
	elif x == "L":
		total += 4.60
	elif x == "P":
		total += 2.85
print(round(total,2))