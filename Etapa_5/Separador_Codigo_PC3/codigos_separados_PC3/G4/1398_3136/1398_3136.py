tdv = float(input("Tempo de voo: "))
mi = (tdv*100) + 5000
lim = (tdv-200)
ma = (200*100) + (lim*90) + 8000

if(tdv<=200):
	print(round(mi, 2))
else:
	print(round(ma, 2))

	