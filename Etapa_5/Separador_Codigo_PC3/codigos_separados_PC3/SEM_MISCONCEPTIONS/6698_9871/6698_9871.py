praca = float(input(""))
pedagio  = 9.8
fixo = 20
icms = 15 / 100
gasto = praca * pedagio + fixo
valor = gasto * icms
total = gasto + valor
print(round(total, 2))
