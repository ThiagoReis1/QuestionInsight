produto = input().upper()

i = 0
total = 0

while i < len(produto):
	if produto[i] == "H":
		total += 3.85
	elif produto[i] == "L":
		total += 2.95
	elif produto[i] == "E":
		total += 7.90
		
	i += 1


print(round(total, 2))