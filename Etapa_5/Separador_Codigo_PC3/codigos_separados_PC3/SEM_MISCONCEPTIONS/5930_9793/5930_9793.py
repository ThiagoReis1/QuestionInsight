pack = float(input("Insira o valor da encomenda: "))

imposto = 0.81 * pack
valtot = imposto + pack + 12

print(round(valtot, 2))