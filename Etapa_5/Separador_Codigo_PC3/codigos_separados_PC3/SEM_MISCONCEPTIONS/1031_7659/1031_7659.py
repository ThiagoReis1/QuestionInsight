quantidade_litros = float(input("digite o valor:?"))
gasolina = 2.86*quantidade_litros+50.00
icms = (gasolina*34)/100
valor_total = gasolina + icms
print(round(valor_total, 2))