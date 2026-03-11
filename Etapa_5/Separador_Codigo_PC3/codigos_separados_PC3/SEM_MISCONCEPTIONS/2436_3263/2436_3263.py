peso = float(input("qual o peso: "))
distancia = float(input("qual a distancia: "))

precopeso = float(25.00)
precokm = float(0.10)
icms = 12

valordepeso = peso * precopeso

valordekm = distancia * precokm

subtotal = valordepeso + valordekm

valorimposto = subtotal * (icms / 100)

precototal = subtotal + valorimposto

print(round(precototal, 2))