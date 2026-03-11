n = int(input('Digite um valor: '))
a = 0
b = 0
c = 0
cont = 0

while cont < n:
	tec = input('Tecnica: ').upper()
	if tec == 'A':
		a = a + 1
	elif tec == 'B':
		b = b + 1
	elif tec == 'C':
		c = c + 1
	cont = cont + 1

print('A=', a)
print('B=', b)
print('C=', c)