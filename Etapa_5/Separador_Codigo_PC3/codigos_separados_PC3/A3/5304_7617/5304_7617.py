# Universidade Federal do Amazonas
# Curso: Estatistica
# Aluno: Nelson Geraldo A. de Carvalho

# Inputs
num_inicial = int(input('Digite o numero inicial de bacterias: '))
qtd_horas = int(input('Digite a quantidade de horas total do experimento: '))

# Variaveis
num = num_inicial
count = 0
aumento_bacterias = 0

# Operacao
while count < qtd_horas:
	# Aumento de Bacterias cresce 15% a cada hora
	# aumento_bacterias = aumento_bacterias + (num + (num * 0.15))
	num = num + int((num * 0.15))
	# Exibindo repetidamente o numero de bacterias a cada hora
	print(num)
	
	# Incrementando count
	count += 1