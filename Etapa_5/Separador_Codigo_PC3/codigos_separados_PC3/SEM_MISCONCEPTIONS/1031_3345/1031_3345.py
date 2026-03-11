gasolina = float(input("Litros de gasolina: "))
valor = (50 + (gasolina * 2.86)) * 1.34
valor_final = round(float(valor), 2)
print(valor_final)