s = input("entre com os pedidos: ").upper()

i = 0
total = 0

while i < len(s):
	if s[i] == 'H':
		total += 3.85
	elif s[i] == 'L':
		total += 2.95
	elif s[i] == 'E':
		total += 7.9
	i += 1
print(round(total,2))