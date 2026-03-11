itens = input("insira a string: ")

i = 0 
total = 0

while i< len(itens):
	if itens[i] == "D":
		total += 2.25
	elif itens[i] == "S":
		total += 4.
	elif itens[i] == "I":
		total += 6.90
	i += 1
print(round(total,2))
	
