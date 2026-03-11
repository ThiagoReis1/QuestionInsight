litros = float(input("litros abastecidos"))
valortotal = float(2.86 * litros + 50.00)
imposto = (valortotal * 0.34)

print(round(imposto * valortotal, 2 ))