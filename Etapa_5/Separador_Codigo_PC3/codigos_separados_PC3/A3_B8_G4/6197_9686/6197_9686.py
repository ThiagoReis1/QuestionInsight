t = 1.6
p = 0.02
l = t+p
ano = 0
a = float(input("a"))
c = float(input("a"))
while True:
	if (a+c*ano) < t + (p*ano):
		ano += 1
	elif (a+c*ano) > (t + p*ano) or c < p:
		break
print(ano)