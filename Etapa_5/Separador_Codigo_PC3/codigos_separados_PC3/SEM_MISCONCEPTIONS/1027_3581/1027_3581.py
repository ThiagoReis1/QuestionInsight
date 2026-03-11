taxa=float(0.43)
valor_fixo=int(10)
icms=float(25/100)
kwh=float(input("digite: "))

conta=taxa*kwh+valor_fixo

valor_total=conta+conta*icms

print(round(valor_total, 2))