comida = input("digite a comida:").upper()

i =0
total = 0

while i < len(comida):
	if comida[i] == "A":
		total += 19.90
	elif comida[i] == "L":
		total += 3.50
	elif comida[i] == "P":
		total += 4.25
	i += 1
	
print(round(total, 2))