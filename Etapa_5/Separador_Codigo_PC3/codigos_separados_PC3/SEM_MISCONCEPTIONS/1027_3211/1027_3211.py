consumo = float(input())
valor_fixo = 10
valor_bruto = 0.43*consumo
ICMS = (valor_bruto + valor_fixo)/4
valor_final = valor_bruto + valor_fixo + ICMS

print(round(valor_final, 2))