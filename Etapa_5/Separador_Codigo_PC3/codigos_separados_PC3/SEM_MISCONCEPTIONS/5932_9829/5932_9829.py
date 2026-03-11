plano = 0.28
valor = 23.00

consumo = float(input("Digite o consumo da chamadas em minutos: "))

taxa = (plano*consumo + valor)*(31/100)

total = plano*consumo + valor + taxa

print(round(total, 2))