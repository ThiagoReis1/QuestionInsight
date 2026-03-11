# Preços dos produtos
preco_adega = 16.75
preco_laticinios = 4.60
preco_padaria = 2.85

# Entrada dos produtos
produtos = input("Digite os produtos (A para adega, L para laticínios, P para padaria): ")

# Inicialização da variável acumuladora para o preço total da compra
total = 0

# Iteração sobre os produtos
for produto in produtos:
    if produto == "A":
      total += preco_adega
      elif produto == "L":
         total += preco_laticinios
      elif produto == "P":
         total += preco_padaria
      else:
         print("Produto inválido:", produto)

# Imprime o valor total da compra com duas casas decimais
print("Valor total da compra:", round(total, 2))