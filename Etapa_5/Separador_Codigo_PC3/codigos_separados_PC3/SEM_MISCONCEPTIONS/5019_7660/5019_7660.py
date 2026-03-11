#---------------------------------------------------------------
# Nome: Ivan Lucas de Oliveira Pacheco
# Data: 21/12/2022
# Objetivo: Definir reajuste de salário anual
#---------------------------------------------------------------

# Ler o valor do salário anual do funcionário
sal = float(input("Qual o valor do salario anual do funcionario? "))

if sal > 0:
	if sal < 1212:
		reajuste = 0.12
	elif sal <= 5000:
		reajuste = 0.08
	else:
		reajuste = 0.03

novo_sal = sal * (1 + reajuste)

print(round(novo_sal,2))