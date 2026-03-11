peso = float(input(" peso da encomenda: "))
if peso <= 4999.9:
	valor = peso*.05
if peso >= 5000.0:
	valor = peso*.04+60
print(round(valor,2))