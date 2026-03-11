minutos = float(input("Digite a quantidade de minutos:"))

mensalidade = 45 + (minutos * 0.97)

imposto = mensalidade * (42/100)

total = mensalidade + imposto

print(round(total,2))