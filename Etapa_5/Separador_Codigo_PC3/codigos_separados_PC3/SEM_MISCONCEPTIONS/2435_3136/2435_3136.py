
preco = float(input("Valor do produto sem desconto: "))

preco_cd = (40 * preco) / 100

pcd = preco - preco_cd

frete = (5 * preco) / 100

print(round(pcd, 2))
print(round(frete, 2))