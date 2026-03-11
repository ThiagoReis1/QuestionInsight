preco_inicio = float(input("preco do inico    "))
preco_final = float(input(" preco do final   "))
porcentagem = ((preco_final - preco_inicio)*100) / preco_inicio
print(round(porcentagem,2))