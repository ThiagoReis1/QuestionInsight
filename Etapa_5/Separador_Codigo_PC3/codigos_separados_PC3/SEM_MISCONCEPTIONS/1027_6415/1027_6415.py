fixo = 10
kwh = float(input("digite quantos kwh consumiu em um mes:"))
custo = kwh * 0.43
taxa = 1.25

valor = (custo + fixo) * taxa

print(round(valor,2))