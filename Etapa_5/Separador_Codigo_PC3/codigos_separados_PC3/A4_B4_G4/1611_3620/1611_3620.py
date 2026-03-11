str = input('str: ')
i = 0
v = 0
c = 0
while i < len(str):
	if str[i] == 'A':
		v = v + 1
	elif str[i] == 'E':
		v = v + 1
	elif str[i] == 'I':
		v = v + 1
	elif str[i] == 'O':
		v = v + 1
	elif str[i] == 'U':
		v = v + 1
	else:
		c = c + 1
	i = i + 1
total = (v * 0.15) + (c * 0.17)
print(round(total, 2))