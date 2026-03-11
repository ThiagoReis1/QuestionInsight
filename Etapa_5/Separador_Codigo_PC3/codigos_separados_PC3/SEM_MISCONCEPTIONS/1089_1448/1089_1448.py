#avaliacao 2. exercicio 1

prim_compra = float(input("Digite o valor da primeira compra:"))
seg_compra = float(input("Digite o valor da segunda compra:"))
terc_compra = float(input("Digite o valor da terceira compra:"))
lim_cartao = float(input("Digite o limite do cartao:"))
val_compra = (prim_compra + seg_compra + terc_compra)
print (round(val_compra, 2))
if (val_compra <= lim_cartao):
	print("Sim")
else:
	print("Nao")
	