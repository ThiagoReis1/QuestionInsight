import math

conta_agua = 0.37
valor_fixo = 15.0

vol_agua_mes = float(input())

conta = (conta_agua*vol_agua_mes) + valor_fixo
aux = (35/100) * conta

result = conta + aux
print(round(result, 2))