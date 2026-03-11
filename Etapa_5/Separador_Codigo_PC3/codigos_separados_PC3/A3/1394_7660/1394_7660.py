#--------------------------------------------
# Nome: Ivan Lucas de Oliveira Pacheco
# Data: 07/12/2022
# Objetivo: Definir o pagamento de professor por horas aula semanais
#--------------------------------------------

# Definição de parâmetro de hora aula
pgto_hora = 50
valor_chave = 20
pagamento_professor = 0

# Leitura da qtde de horas aula ministradas semanalmente
aula_semanal = float(input("Defina a quantidade de horas aula semanais do professor: "))

if aula_semanal > valor_chave:
	pagamento_professor = valor_chave * pgto_hora
	aula_semanal = aula_semanal - valor_chave
	pgto_hora = 70

pagamento_professor = pagamento_professor + (aula_semanal * pgto_hora)

print(round(pagamento_professor,2))