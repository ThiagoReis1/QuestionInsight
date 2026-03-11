#av 01, exercicio 2
#Caio Fernandes
TrocaDeOleo = 50.0
icms = 34/100
PrecoDoLitro = 2.86
Abastecido = float(input("digite o valor de Litros abastecidos: "))
total = (PrecoDoLitro * Abastecido + TrocaDeOleo)
imposto = total * icms
print(round(total + imposto,2))