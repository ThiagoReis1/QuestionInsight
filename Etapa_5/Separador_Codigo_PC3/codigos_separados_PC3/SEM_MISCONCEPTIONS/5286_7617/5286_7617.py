# Universidade Federal do Amazonas
# Curso: Estatistica
# Aluno: Nelson Geraldo A. de Carvalho

# Inputs
num = int(input('Digite um numero (0 para encerrar): '))

# Variaveis
total = 0
count_mult_dois = 0
mult_dois = []

# Operacoes
while (num != 0):
	# Verifica se o numero e divisivel por 2
	if (num % 2 == 0):
		# Acrescenta no Array o numero divisivel por 2
		mult_dois.append(num)
		# Incrementa contagem do total de numeros divisiveis por 2
		count_mult_dois += 1
	
	# Incrementa total da contagem
	total += 1
	num = int(input('Digite um numero (0 para encerrar): '))

# Definindo a Porcentagem
porcentagem_mult_dois = (count_mult_dois / total) * 100

# Outputs
print(total)
print(round(porcentagem_mult_dois, 2))
