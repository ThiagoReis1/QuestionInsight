quilo_mercadoria = 43.21
taxa_fixa = 25.00

peso_mercadoria = float(input())

preco_mercadoria = (peso_mercadoria * quilo_mercadoria)

preco_total = preco_mercadoria + taxa_fixa

icms = preco_total * 0.62

preco_final = preco_total + icms 

print(round(preco_final,2))