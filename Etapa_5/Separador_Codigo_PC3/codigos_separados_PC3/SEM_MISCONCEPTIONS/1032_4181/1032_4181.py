valor = float(input("Valor da encomenda: "))
taxa = 12

imposto = valor*81/100

vt = valor + imposto + taxa

print(round(vt, 2))