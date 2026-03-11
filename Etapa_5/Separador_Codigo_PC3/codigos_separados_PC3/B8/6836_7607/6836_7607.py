comidas = input("Digite as comidas compradas: ").upper()

total = 0
i = 0 

while i < len(comidas): 
	if comidas[i] == "B": 
		total += 6.8
	elif comidas[i] == "C":
		total += 11.75
	elif comidas [i] == "M":
		total += 5.9
		
	i += 1
	
print(round(total,2))