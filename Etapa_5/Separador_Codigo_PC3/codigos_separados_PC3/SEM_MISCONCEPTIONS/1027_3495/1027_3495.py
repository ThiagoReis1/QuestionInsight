kwh=float(0.43)

mes = float(input())

consumo = float((mes*kwh)+10)
imposto=float(0.25*consumo)
val=float(consumo+imposto)

print(round(val,2))
