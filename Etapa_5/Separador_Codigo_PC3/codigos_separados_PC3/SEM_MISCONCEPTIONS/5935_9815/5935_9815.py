peso = float(input("Peso da Mercadoria em Kg: "))
semimposto = (peso * 43.21) + 25
comimposto = round(semimposto + (semimposto * 62 / 100), 2)
print(comimposto)