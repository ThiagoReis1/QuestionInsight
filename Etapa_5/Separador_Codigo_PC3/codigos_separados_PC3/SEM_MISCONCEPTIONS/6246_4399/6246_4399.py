result = str(input())
result = result.upper()
vitorias_A = 0

while(result != 'X'):
	if result == 'A':
		vitorias_A += 1
	result = str(input())
	result = result.upper()

print(vitorias_A)