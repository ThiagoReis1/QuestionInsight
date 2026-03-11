item = input("insira o item desejado: ")

i = 0 
total = 0 

while i < len(item):
	if item[i] == "H":
		total += 3.85
	elif item[i] == "L":
		total += 2.95
	elif item[i] == "E":
		total += 7.90
	i += 1
print(round(total, 2))