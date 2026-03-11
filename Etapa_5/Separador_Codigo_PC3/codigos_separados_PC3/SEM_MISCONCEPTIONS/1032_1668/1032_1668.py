valor_encomenda = float(input("Qual o valor da encomenda?"))
imposto_importacao = 0.81
taxa_fixa = 12.0
valor_total = valor_encomenda +valor_encomenda * imposto_importacao + taxa_fixa
print(round(valor_total, 2))