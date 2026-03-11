peso = float(input("Digite o peso do produto: "))
distancia = float(input("Digite a distancia entre o ponto de origem e destino: "))
kg = 25
km = 0.10
icms = kg*peso + km * distancia * 0.12

preco_total = kg * 25 + distancia * km + icms
print(round(preco_total, 2))