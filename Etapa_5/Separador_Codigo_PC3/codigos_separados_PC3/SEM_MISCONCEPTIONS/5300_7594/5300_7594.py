velocidade = float(input())
minutos = 0

while velocidade >= 50:
	print(round(velocidade, 2))
	velocidade = velocidade - velocidade*(25/100)
	minutos = minutos + 1