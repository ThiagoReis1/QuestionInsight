# valor da compra
v_c = float(input("digite o valor da compra:"))
#  valor imposto
v_i = 81/100 * v_c
# taxa fixa agencia dos correios
t_f = 12
# custo total
custo_total = v_c + v_i + t_f
print(round(custo_total,2))