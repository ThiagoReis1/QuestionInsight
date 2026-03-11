nome = input("Digite o nome da Unidade Academica: ")
					
soma = 0

while	(nome.upper() != 'S'):
	if	(nome.upper() == 'ICOMP'):
		soma = soma + 1
	nome = input("Digite o nome da Unidade Academica: ")
print(soma)