feira = input("produtos da secao").upper()

i = 0
total = 0

while i < len(feira):
	if feira[i] == "H":
		total += 3.85
	elif feira[i] == "L":
		total += 2.95
	elif feira[i] == "E":
		total += 7.90
	
	i += 1
print(round(total, 2))