pvs = input().upper()
c = 0
i = 0

while (pvs == 'PRETA' or pvs == 'VERMELHA' or pvs == 'S'):
	i = i + 1
	if pvs == 'PRETA':
		c = c + 1
	p = (c / i) * 100
	if pvs == 'S':
		print(i - 1)
		print(round((( c / (i - 1)) * 100), 2))
		break
	pvs = input('').upper()
	
