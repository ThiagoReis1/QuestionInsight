item = input("bota:")

i = 0
total = 0

while i < len(item):
	if item[i] == "C":
		total +=10.50
	elif item[i] == "E":
		total += 8.75
	elif item [i] == "P":
		total +=17.90
	i +=1
	
print(round(total, 2))
		