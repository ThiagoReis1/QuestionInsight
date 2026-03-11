it = input("Itens: ").upper()

i = 0
ttl = 0

while i < len(it):
	if it[i] == "B":
		ttl += 6.8
	elif it[i] == "C":
		ttl += 11.75
	elif it[i] == "M":
		ttl += 5.9
	i += 1
	
print(round(ttl,2))