color = input()
color = color.upper()
times = 0

while color != 'S':
	if color == 'PRETA':
		times += 1
	color = input()
	color = color.upper()
print(times)