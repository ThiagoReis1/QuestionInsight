quantidade = float(input("litros abastecidos: "))
gasolina = 2.86
oleo = 50
imposto = ((gasolina*quantidade)+oleo)*0.34
total = ((gasolina*quantidade)+oleo)+imposto
print(round(total,2))