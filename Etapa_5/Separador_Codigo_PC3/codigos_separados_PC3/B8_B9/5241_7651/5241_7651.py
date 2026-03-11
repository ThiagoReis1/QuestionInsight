consumo = float(input())

if (consumo<10):
	total = (consumo*2)+20
	print(round(total,2))
elif (consumo>=10 and consumo<20):
	total = (consumo*2.5)+20
	print(round(total,2))
elif (consumo>=20 and consumo<40):
	total = (consumo*2.75)+20
	print (round(total,2))
elif (consumo>=40):
	total = (consumo*3)+20
	print (round(total,2))