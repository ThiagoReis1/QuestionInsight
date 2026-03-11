preco_litro=2.86
troca_oleo=50.00
litros_abastecidos= float(input("digite os litros"))
valor_litros_abastecidos= preco_litro*litros_abastecidos
valor= valor_litros_abastecidos + troca_oleo
aplicacao=valor*34/100
total_pago = valor + aplicacao
print(round(total_pago,2))
