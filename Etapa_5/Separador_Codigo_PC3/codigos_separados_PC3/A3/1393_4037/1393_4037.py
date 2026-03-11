peso=float(input('peso da encomenda: '))


if peso<=4999.9:
	mensagem=peso*0.05
if peso>=5000.0:
	mensagem=(peso*0.04) + 60.00

print(round(mensagem, 2))