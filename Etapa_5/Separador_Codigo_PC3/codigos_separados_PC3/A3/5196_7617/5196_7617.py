# Universidade Federal do Amazonas
# Aluno: Nelson Geraldo A. de Carvalho
# Curso: Estatistica

# Se valor do Prod. Antigo <= 100.00 -> aumento de 5%
# Se valor do Prod. Antigo > 100.00  -> aumento de 15%

novo_valor = 0
mensagem = ''

# Inputs 
valor_antigo = float(input('Digite o valor do produto antigo: '))

# Calculo
if(valor_antigo <= 100):
	porcentagem = valor_antigo * 0.05
	novo_valor = valor_antigo + porcentagem
	mensagem = 'Aumento de 5 porcento'
else:
	porcentagem = valor_antigo * 0.15
	novo_valor = valor_antigo + porcentagem
	mensagem = 'Aumento de 15 porcento'

# Outputs
print(round(novo_valor, 2), 'ryous')
print(mensagem)