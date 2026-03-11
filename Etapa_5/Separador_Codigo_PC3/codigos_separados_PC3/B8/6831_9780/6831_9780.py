prdt = input("Coloque os produtos que voce comprou:  ").upper()
i = 0
total = 0 
while i < len(prdt):
	if prdt[i] == "A":
		total += 16.75
	elif prdt [i] == "L":
		total += 4.60
	elif prdt [i] == "P":
		total += 2.85
		
	i += 1 
print(round(total,2))