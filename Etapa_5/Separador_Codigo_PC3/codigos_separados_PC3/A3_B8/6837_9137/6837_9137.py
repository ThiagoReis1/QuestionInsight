produtos = input().upper()

total = 0
i = 0
I = 0
M = 0
S = 0

while i < len(produtos):
	if produtos[i] == "I":
		total += 3.75
	elif produtos[i] == "M":
		total += 4.5
	elif produtos[i] == "S":
		total += 2.9
	i += 1
print(round(total, 2))