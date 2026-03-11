alm = 1.86
tm = 0.01
alg = float(input("Altura gato: "))
tg = float(input("Taxa de crescimento: "))
c = 0
while alg <= alm:
	alm = alm + tm
	alg = alg + tg
	c = c + 1
print(c)