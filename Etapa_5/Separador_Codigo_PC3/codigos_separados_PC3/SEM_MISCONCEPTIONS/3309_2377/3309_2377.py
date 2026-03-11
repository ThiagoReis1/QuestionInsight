# Entrada de variaveis para despacho de mercadorias vendidas

mercadoria_kg = 43.21
taxa_mercadoria = 25
porcentagem = 0.62

# Entrada do comando para despacho de mercadorias vendidas

comando = float(input("Digite a quantidade de quilo transportado: "))
peso_mercadoria = (mercadoria_kg * comando) + taxa_mercadoria + porcentagem

print(round(peso_mercadoria,2))


# Saida do comando para despacho de mercadorias vendidas

