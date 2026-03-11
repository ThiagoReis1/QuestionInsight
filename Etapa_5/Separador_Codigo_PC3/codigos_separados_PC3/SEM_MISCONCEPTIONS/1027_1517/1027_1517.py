
consumo = float(input())

custoKwh = 0.43
taxaFixa = 10
icms = 0.25

total = (consumo * custoKwh + taxaFixa)
imposto = total * icms
total = total + imposto

print(round(total, 2))