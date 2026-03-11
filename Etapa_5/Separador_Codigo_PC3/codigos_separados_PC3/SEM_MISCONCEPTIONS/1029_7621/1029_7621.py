telef = 0.28
valfix = 23


minutos = float(input("numero de minutos consumidos em um mes: "))
valorconsumido = (telef*minutos) + valfix
valor_total = (valorconsumido)*(0.31) + valorconsumido
print(round(valor_total, 2))