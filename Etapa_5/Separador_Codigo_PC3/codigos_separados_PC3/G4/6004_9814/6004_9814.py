t = int(input('Quantidade de tomates: '))

tma = round(t * 0.55, 2)
tme = round(t * 0.75, 2)
if t >= 4:
	print(tma)
else:
	print(tme)