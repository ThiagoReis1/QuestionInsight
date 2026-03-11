peso=float(input("peso da mercadoria:"))

preco=((43.21*peso)+25)

com_imposto=((preco*(62/100))+preco)

print(round(com_imposto,2))