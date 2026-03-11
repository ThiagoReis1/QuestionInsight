c1 = int(input('Candidato mais votado: '))
c2 = int(input('Segundo lugar: '))
c3 = int(input('Menos votado: '))
branco = int(input('Brancos: '))
nulo = int(input('Nulos: '))
soma = c1 + c2 + c3
if c1 > soma * 0.5:
	print('NAO')
else:
	print('SIM')