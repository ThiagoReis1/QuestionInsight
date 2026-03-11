count = 0 
color = input().upper()
while color != 'S':
	if color == 'PRETA':
		count += 1
	color = input().upper()
print(count)