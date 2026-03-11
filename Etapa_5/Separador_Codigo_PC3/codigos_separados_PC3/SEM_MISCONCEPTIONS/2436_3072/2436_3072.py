kg = 25.00
km = 0.10
icms = 12

peso = int(input("Entre com o peso do produto: "))
distancia = int(input("Entre com a distancia: "))

preco = (peso * kg) + (distancia * km)
preco_ICMS = preco * (icms / 100)
preco_Total = preco + preco_ICMS

print(round(preco_Total, 2))