from numpy import*

i = 0
p = 0
s = input('Digie a etiqueta dejejada: ').upper()
#print(s[0])

while i < len(s):
	if s[i] == 'A' or s[i] == 'E' or s[i] == 'O' or s[i] == 'U' or s[i] == 'I':
		p = p + 0.19
	else:
		p = p + 0.23
	i += 1
print(round(p,2))
