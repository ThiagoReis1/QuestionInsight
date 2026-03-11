produto =input()
i = 0
total = 0 
while i != len(produto):
	if produto[i] == 'M':
		total += 7.25
	elif produto[i] == 'P':
		total += 4.75
	elif produto[i] == 'R':
		total += 3.50
	i = i + 1
	
print(round(total,2))