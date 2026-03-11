L_ou_S = (input("Lanche ou Salgado"))
quantidade = int(input("Quantidade"))
refri = int(input("Quantidade de Refri"))

preco_L = 5
preco_S = 3.5
preco_refri = 4

if L_ou_S == "S":
	preco_final = preco_S * quantidade + preco_refri * refri
else:
	preco_final = preco_L * quantidade + preco_refri * refri

preco_final = round(preco_final,2)
print(preco_final)