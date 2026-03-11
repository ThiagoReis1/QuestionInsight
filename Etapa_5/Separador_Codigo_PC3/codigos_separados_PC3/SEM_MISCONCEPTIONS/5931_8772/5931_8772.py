qtde_min = float(input())

plano = 45 + 0.97 * qtde_min
icms = 0.42 * plano
total = plano + icms

print(round(total, 2))