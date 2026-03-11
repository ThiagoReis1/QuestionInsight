kg= float(input("Peso da mercadoria: "))
preco_kg=float((kg*43.21) + 25)

imposto= float((preco_kg*62)/100)

valor_total=float(preco_kg+imposto)

print(round(valor_total,2))