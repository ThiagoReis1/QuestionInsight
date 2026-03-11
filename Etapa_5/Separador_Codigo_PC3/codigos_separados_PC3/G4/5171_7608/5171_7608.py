peso = float(input("Peso do saco: "))
qtd = float(input("Quantidade diaria: "))
dias = 7
qtd_rest = peso - (qtd * dias)
print(round(qtd_rest, 2))