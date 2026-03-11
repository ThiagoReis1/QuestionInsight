quantidade_de_minutos = float(input("digite a quantidade de minutos: "))
plano = 45 + (0.97 * quantidade_de_minutos)
aumento = plano + (plano * 0.42)
print(round(aumento,2))
