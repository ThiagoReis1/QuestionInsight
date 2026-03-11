#gasolina 2,86 reais
#oleo 50.00 reais
#imposto de 34%
#193.0
#65.62

quantidade_litros = float(input("Quantos litros foram abastecidos? "))
oleo = 50.00
imposto = 34 
preco_gasolina = 2.86
gasolina = quantidade_litros * preco_gasolina + oleo 
gasolina_2 = imposto*gasolina
gasolina_3 = gasolina_2 / 100
gasolina_imposto = gasolina + gasolina_3

print(round(gasolina_imposto,2))

