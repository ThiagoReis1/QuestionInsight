string = input().upper()

i = 0
soma = 0

while i < len(string):
	if	string[i] == 'H':
		soma +=5.4
	elif	string[i] == 'C':
		soma +=8.95
	elif	string[i] == 'L':
		soma += 4.5
	i+=1
print(round(soma,2))