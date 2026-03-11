valor = float(input("Valor da encomenda: "))

imposto = 81/100
taxa = 12

total1 = valor * imposto
total = total1 + valor + taxa

print(round(total, 2))