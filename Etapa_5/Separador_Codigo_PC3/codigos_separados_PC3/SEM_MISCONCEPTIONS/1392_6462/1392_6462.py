conta = 30
vol = float(input("valor: "))

if vol < 10:
	contaf = conta + 3*vol
else:
	contaf = conta + (3.50)*(vol)
print(round(contaf,2))