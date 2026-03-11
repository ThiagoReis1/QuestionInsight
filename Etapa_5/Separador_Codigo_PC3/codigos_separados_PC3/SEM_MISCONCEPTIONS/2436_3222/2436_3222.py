peso = float(input("Peso do produto: "))
d = float(input("Distancia: "))

preco = ((peso * 25.00) + (d * 0.10))
imposto = preco * 0.12
x = preco + imposto

print(round(x, 2))