#---------------------------------------
# Nome: Ivan Lucas de Oliveira Pacheco
# Data: 21/11/2022
# Objetivo: Calcular o valor total a ser pago pela troca de oleo e abastecimento de um veiculo
#---------------------------------------

# Definição de Constantes
troca_oleo = 50
preco_gasolina = 2.86
icms = 0.34

# Leitura de litros
litros_abastecidos = float(input("Qual a quantidade de litros abastecidos? "))

# Calculo do valor total gasto
valor_imposto = (troca_oleo + (preco_gasolina * litros_abastecidos)) * icms
valor_total = troca_oleo + (preco_gasolina * litros_abastecidos) + valor_imposto

# Impressão do valor a ser pago
print(round(valor_total,2))