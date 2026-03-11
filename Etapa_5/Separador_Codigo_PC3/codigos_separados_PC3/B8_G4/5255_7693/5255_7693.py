p = float(input("digite o peso da mercadoria: "))
d = float(input("digite a distancia da entrega da mercadoria: "))
cod = int(input("digite o codigo do estado de destino: "))

ckg = p*25
ckm = d*0.1

if cod == 1:
	total = (ckg + ckm)*1.17
	print(round(total, 2))
elif cod == 2:
	total = (ckg+ckm)*1.175
	print(round(total, 2))
elif cod == 3:
	total = (ckg+ckm)*1.18
	print(round(total, 2))
elif cod == 4:
	total = (ckg+ckm)*1.20
	print(round(total, 2))
