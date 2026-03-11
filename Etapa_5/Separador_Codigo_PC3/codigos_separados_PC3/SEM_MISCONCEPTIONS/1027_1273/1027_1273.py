
kwh_consumido=float(input())
cada_kwh=0.43
valor_fixo=10.

total_dos_gastos= kwh_consumido * cada_kwh + valor_fixo
total_conta= total_dos_gastos + total_dos_gastos * 0.25

print(round(total_conta,2))

