hort = 5.40
cereais = 8.95
lac = 4.50

l1 = input().upper()
i = 0
total = 0

while i <len(l1):
	if l1[i] == "H":
		total += hort
	elif l1[i] == "C":
		total +=cereais
	elif l1[i] == "L":
		total += lac
	i += 1
print(round(total,2))