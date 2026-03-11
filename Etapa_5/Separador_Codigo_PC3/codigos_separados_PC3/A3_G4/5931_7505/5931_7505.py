qtd = float(input())

plano = 45
exc = 0.97
icms = 0.42
exp = qtd*0.97
exp0 = ((exp+plano)*icms)+(exp+plano)

print(round(exp0, 2))