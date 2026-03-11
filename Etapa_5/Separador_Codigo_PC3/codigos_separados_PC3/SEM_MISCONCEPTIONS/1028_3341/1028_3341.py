volume = float(input("numero"))
custo_metro3 = 0.37 * volume
valor_fixo = 15.00
total = custo_metro3 + valor_fixo
imposto = (35 * total)/100
var_mes = total + imposto
print(round(var_mes, 2))