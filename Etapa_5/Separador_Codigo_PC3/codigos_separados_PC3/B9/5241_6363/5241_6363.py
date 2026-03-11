consumo = int(input("consumo da agua: "))

if(consumo<10):
	x = consumo*2.0+20
elif((consumo>=10) and (consumo<20)):
	x = consumo*2.5+20
elif((consumo>=20) and (consumo<40)):
	x = consumo*2.75+20
else:
	x = consumo*3.0+20
print(round(x, 2))
