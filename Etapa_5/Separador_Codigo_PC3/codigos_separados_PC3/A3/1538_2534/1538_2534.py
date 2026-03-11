x = float(input("x "))
k = int(input("k "))

serie = x
i = 0
sinal = +1

while(-1 < x < +1):
	serie = serie + (1 - x*2 + x*4 - x*6 + x*8)
	i = i + 1
	sinal = sinal * -1

print(round(serie,8))