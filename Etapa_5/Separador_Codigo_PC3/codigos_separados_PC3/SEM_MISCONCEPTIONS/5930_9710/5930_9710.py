taxa = 12.00
imposto = 81.0/100
encomenda = float(input("qantidade encomenda"))

valor = encomenda+imposto*encomenda
total = (valor+taxa)
print(round(total,2))