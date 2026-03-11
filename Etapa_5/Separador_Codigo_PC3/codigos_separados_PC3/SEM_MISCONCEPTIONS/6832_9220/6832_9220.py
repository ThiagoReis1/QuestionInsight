prod = input().upper()

i = 0
total = 0

while i < len(prod):
	if prod[i] == "H":
		total += 5.4
	if prod[i] == "C":
		total += 8.95
	if prod[i] == "L":
		total += 4.5
	i += 1
print (round(total,2))
