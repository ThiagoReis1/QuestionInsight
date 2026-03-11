preco_l = 2.86
t_oleo = 50.00
icms = 0.34
ql = float(input('Digite a quantidade de litros: '))
v1 = (preco_l * ql)
v2 = (v1 + t_oleo)
v3 = (v2 * 34/100)
v4 = (v2 + v3)
print(round(v4, 2))


