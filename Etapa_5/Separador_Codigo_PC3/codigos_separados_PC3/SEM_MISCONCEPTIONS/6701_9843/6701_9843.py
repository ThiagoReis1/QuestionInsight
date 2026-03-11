valor = float(input("Digite o valor total dos produtos: "))
total = valor + 15
icms = total * 0.3

final = total + icms

print(round(final, 2))