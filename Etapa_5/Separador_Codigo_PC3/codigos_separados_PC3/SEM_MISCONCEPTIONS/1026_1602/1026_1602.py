lado = float(input("qual o tamanho do lado ?"))
preco = float(input("qual o preço por metro ?"))

tamanho=lado*6
preco_total = tamanho * preco
print(round(preco_total,2))
