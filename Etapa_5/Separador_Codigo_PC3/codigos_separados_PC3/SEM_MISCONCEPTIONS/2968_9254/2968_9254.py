comida = input("Salgado ou lanche: ")
qtd = int(input("quantidade: "))
refri = int(input("refrigerante: "))

preco_lanche = qtd * 5 + refri * 4 
preco_salgado = qtd * 3.5 + refri * 4

if comida.upper() == "L":
	print(round(preco_lanche, 2))
else:
	print(round(preco_salgado, 2))