valor = float(input("Valor de uma encomenda: "))
imposto = valor * 0.81
taxa = valor + imposto + 12

valor_total = taxa
print(round(valor_total, 2))