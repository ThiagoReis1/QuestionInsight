#-----------------------------------------
# Nome: Ivan Lucas de Oliveira Pacheco
# Data: 21/11/2022
# Objetivo: Definir a quantidade de ração restante no saco ao final de 1 semana
#-----------------------------------------

# Leitura do valor do peso do saco de ração e a quantidade diária
peso_saco_racao = float(input("Qual o peso do saco de racao em gramas? "))
qtd_diaria = float(input("Qual a quantidade diaria da porcao em gramas? "))

# Calculo
peso_saco_racao = peso_saco_racao - (qtd_diaria * 7)

# Impressão do peso restante no saco de ração
print(round(peso_saco_racao,2))
