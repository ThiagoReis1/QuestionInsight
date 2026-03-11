altura_alice = 1.6
taxa_alice = 0.02

altura_aluno = float(input('altura inicial da aluno: '))
taxa_aluno = float(input('taxa de crecimento da aluno: '))

ano = 0 # contadora

while altura_aluno < altura_alice:
	altura_alice = altura_alice + taxa_alice
	altura_aluno = altura_aluno + taxa_aluno
	ano += 1
	# print('ano: ', ano, 'alt_aluno: ', altura_aluno, 'alt_aluno: ', altura_aluno)
	
print(ano)
	