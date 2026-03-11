ca = 0
soma = 1
i = 0

while ca != 'X':
	ca = input().upper()
	if ca == 'FT':
		soma = soma + i
		i += 1	
print(i)