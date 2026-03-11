unidade = input('Unidade Academica: ').upper()

alunos_ft = 0

while (unidade != 'X'):
	if unidade == 'FT':
		alunos_ft += 1
	unidade = input('Unidade Academica: ').upper()
print(alunos_ft)