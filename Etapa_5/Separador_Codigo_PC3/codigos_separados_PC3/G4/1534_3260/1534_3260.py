x = float(input("x = "))
k = int(input("termos da serie = "))

tg = 0

while k > 0:
	tg = tg + ((x ** (k * 2 - 1)) / (k * 2 - 1))
	k = k - 1

print(round(tg ,7))