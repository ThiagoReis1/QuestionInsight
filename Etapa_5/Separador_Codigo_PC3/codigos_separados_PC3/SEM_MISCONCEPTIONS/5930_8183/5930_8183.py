var1 = float(input("Digite o valor da ecomenda: RS "))

taxa = 12.00

imposto = var1 * (81/100)

total = imposto + var1 + taxa

print(round(total, 2))