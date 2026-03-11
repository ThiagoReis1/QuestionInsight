x = float(input())

raiz = 0
if -4 <= x < 0:
	raiz = abs(x) ** (1/2)
	print(round(raiz, 4))
elif 0 <= x <= 4:
	raiz = x ** (1/2)
	print(round(raiz, 4))
else:
	print('entrada invalida')
