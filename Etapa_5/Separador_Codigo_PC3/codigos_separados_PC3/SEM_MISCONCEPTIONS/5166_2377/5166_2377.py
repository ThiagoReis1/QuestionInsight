# Entrada de Variaveis para Racao de Passaros

peso_saco = float(input("Digite o peso do saco de racao: "))
quantidade_saco = float(input("Digite a quantidade de racao diaria: "))

# Saida de variaveis para racao de passaros

saida_racao = quantidade_saco * 3

valor_total = (saida_racao * 5)

valor_extra = peso_saco - valor_total


print(round(valor_extra,2))