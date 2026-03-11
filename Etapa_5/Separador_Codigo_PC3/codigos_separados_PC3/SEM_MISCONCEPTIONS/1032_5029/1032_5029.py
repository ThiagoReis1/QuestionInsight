valor_encomenda = float(input("Valor da encomenda: "))
imposto = (valor_encomenda*81)/100
taxa = 12
total = valor_encomenda+imposto+taxa
print(round(total, 2))