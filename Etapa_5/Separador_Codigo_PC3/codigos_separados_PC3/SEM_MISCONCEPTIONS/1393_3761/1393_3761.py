p = float(input('peso da encomenda: '))

if(p >= 5000):
	cobranca = (p*0.04) + 60
else:
	cobranca = (p * 0.05)

print(round(cobranca, 2))	