s = input('aqui:')
i = 0
soma = 0

while i < len(s):
	if s[i] == 'H':
		soma = soma + 3.85
	elif s[i] == 'L':
		soma = soma + 2.95
	elif s[i] == 'E':
		soma = soma + 7.9
	i = i + 1

print(round(soma, 2))