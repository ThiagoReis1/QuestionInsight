s = input("Digite a palavra: ").upper()
i = 0
soma = 0
while i < len(s):
	if s[i] == 'A':
		soma = soma + 45.12
	elif s[i] == 'E':
		soma = soma + 45.12
	elif s[i] == 'I':
		soma = soma + 45.12
	elif s[i] == 'O':
		soma = soma + 45.12
	elif s[i] == 'U':
		soma = soma + 45.12
	else: 
		soma = soma + 50.18 
	i = i + 1
print(round(soma,2))
		