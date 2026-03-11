kwh_consumidos = float(input("Determine quantos kwh foram consumidos no mes: "))

conta = (0.43 * kwh_consumidos) + 10.0

ICMS = conta * 0.25

valor_total = conta + ICMS

print(round(valor_total, 2))


