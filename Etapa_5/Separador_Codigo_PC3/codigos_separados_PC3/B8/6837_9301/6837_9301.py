s = input("s: ")
preco_total = 0
for i in range(len(s)):
	if s[i] == "I":
		preco_total += 3.75
	elif s[i] == "M":
		preco_total += 4.50
	elif s[i] == "S":
		preco_total += 2.90
preco_total = round(preco_total,2)
print(preco_total)
		