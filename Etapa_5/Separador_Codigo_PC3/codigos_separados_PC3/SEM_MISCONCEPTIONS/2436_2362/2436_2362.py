peso = float(input(":"))
distancia = float(input(":"))

kg = 25
km = 0.10
icms = 12/100

preco = peso*kg + distancia*km

imposto = preco*icms

total = preco + imposto

print(round(total,2))

