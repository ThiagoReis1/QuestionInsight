min_ex = float(input("Digite a quantidade de minutos excedentes do plano: "))

plano = 45 + min_ex * 0.97
icms = 142/100
total = plano * icms

print(round(total, 2))