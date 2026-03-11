quantia_cambio = float(input("Qual a quantia que o cliente entrega?"))
valor_dolar = 3.55
valor_taxa = 12.00
custo_total = (quantia_cambio - valor_taxa) / valor_dolar
print(float(custo_total, 2))