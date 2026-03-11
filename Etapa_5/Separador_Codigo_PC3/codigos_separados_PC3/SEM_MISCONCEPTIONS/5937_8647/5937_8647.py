quantidade_litros = float(input("Qual a quantidade de Litros abastecida?: "))

preco_litro = 2.86
troca_oleo = 50.0

valor_consumo = quantidade_litros * preco_litro + troca_oleo

acrescimo = valor_consumo + valor_consumo* (34/100)

print(round(acrescimo, 2))