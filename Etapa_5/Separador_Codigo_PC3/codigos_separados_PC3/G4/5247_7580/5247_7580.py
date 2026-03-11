s = float(input(': '))
c = int(input(': '))
if c == 101:
	s += s*(0.80/100)
elif c == 102:
	s += s*(0.65/100)
elif c == 103:
	s += s*(0.60/100)
elif c == 104:
	s += s*(0.55/100)
else:
	print('Dados invalidos')
if c == 101 or c == 102 or c == 103 or c == 104:
	print('Novo salario: R$ {}'.format(round(s,2)))