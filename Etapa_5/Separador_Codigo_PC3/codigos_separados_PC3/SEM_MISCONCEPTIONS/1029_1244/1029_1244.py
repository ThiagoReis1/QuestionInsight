# Kamila Dias Preira
# 16 de junho de 2016
# 1 Avaliação de ICC

min_consumido = float(input("Consumo de chamadas: "))

# Consumo de chamadas (em minutos) durante certo mês:100
valor = (min_consumido * 0.28 + 23)
ICMS = valor * 0.31
total = valor + ICMS

print(round(total, 2))