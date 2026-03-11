# faça seu código aqui!
v = float(input("V: "))
assinatura = 60
if v < 50:
	total = assinatura + 4.5
	print(round(total, 2))
elif v == 50:
	total = assinatura + 5.5
	print(round(total, 2))
else:
	total = assinatura + 6.5
	print(round(total, 2))