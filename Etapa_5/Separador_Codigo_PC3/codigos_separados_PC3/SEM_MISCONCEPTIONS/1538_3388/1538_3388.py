x = float(input())
k = int(input())
s = 1
sinal = -1
ind = 2
contador = 1

while k > contador:
	s = s + ((x**ind) * sinal)
	sinal = sinal * (-1)
	ind = ind + 2
	contador = contador + 1
print(round(s,8))
