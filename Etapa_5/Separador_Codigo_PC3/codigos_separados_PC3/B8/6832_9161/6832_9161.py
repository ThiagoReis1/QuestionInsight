hortifruti = input(" : ").upper()

i = 0
total = 0
while i < len(hortifruti) :
	if hortifruti[i] == "H" :
		total += 5.40
	elif hortifruti[i] == "C" :
		total += 8.95
	elif hortifruti[i] == "L" :
		total += 4.50
	i += 1
print(round(total, 2))