x = float(input("Numero real a ser analisado: "))
k = int(input("Numero de termos a serem considerados: "))
arc = 0
while(k > 0):
	c = 2 * k - 1
	t = (x**c)/c
	arc = arc + t
	k = k - 1
print(round(arc, 7))