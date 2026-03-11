

st = input().upper()
tam = len(st)

i = 0
soma = 0
while i < tam:
	if st[i] == 'M':
		t = 0 + 7.25
		soma = soma + t
	elif st[i] == 'P':
		t = 0 + 4.75
		soma = soma + t
	elif st[i] == 'R':
		t = 0 + 3.50
		soma = soma + t
	i += 1
print(round(soma,2))