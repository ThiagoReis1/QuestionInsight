s = input("Insira os pedidos:").upper()
i = 0
total = 0
while i < len(s):
	if s[i] == 'H':
		total += 5.40
	elif s[i] == 'C':
		total+=8.95
	elif s[i] == 'L':
		total+=4.50
	i+=1
print(round(total,2))