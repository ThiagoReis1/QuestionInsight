produto = input().upper()

i = 0
soma = 0

while i < len(produto):
	if produto[i] == 'A':
		soma += 19.9
	elif produto[i] == 'L':
		soma += 3.5
	elif produto[i] == 'P':
		soma += 4.25
	i += 1
print(round(soma,2))
		