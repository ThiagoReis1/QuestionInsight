produto = input("digite uma string: ")

total = 0

while  :
	if produto == "I":
		total = total + 3.75
		
	if produto == "M":
		total = total + 4.50
		
	if produto == "S":
		total = total + 2,90
		
print(round(total, 2))