n = int(input('qdd funcionarios: '))
c = 0
a = 0
b = 0
count = 0

while count < n :
	tec = input('qual a tecnica escolhida? ').upper
	if tec == 'A':
		a = a + 1
	elif tec == 'B':
		b = b+1
	elif tec == 'C':
		c = c + 1

	count = count + 1 
print('A= ', a)
print('B= ', b)
print('C= ', c)
