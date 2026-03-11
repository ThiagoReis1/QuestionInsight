# Universidade Federal do Amazonas
# Aluno: Nelson Geraldo A. de Carvalho
# Curso: Estatistica

# Inputs
senha = input('Digite a senha que voce deseja: ').upper()

# Constantes 
custo_vogal = 1.12
custo_consoante = 1.18

# Variaveis Acumuladoras
i = 0
custo = 0

# Operacao de Calculo do Custo Total
while i < len(senha):
	if senha[i] == 'A' or senha[i] == 'E' or senha[i] == 'I' or senha[i] == 'O' or senha[i] == 'U':
		custo += custo_vogal
	else:
		custo += custo_consoante
	i += 1
	
# Outputs
print(round(custo, 2))