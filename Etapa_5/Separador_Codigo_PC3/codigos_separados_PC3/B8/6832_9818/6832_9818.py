from numpy import *
item = input("produto: ")
i = 0
total = 0
while i < len(item):
	if item[i] == "H":
		total += 5.40
	elif item[i] == "C":
		total += 8.95
	elif item[i] == "L":
		total += 4.50
	i += 1
print(round(total, 2))
	