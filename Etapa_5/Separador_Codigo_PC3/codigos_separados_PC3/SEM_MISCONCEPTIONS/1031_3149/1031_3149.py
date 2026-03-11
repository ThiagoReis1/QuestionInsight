litros = float(input("Litros: "))
preco_gasolina = litros * 2.86
valor_oleo = 50.00
preco_total = (preco_gasolina + valor_oleo) * 0.34 + (preco_gasolina + valor_oleo)
print(round(preco_total, 2))