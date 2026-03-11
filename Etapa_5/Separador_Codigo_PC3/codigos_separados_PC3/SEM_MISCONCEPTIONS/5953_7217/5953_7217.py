xsalada_ou_feijoada=input("x/f:")
quantidade_de_pratos=input("quantidade_x")
quantidade_de_bebidas=input("quantidade_f")

if xsalada_ou_feijoada== "x":
	valor_total=float(quantidade_de_pratos*13.50)+(quantidade_de_bebidas*3)
else:
	valor_total=(quantidade_de_pratos*6)+(quantidade_de_bebidas*3)
print(valor_total,2)

