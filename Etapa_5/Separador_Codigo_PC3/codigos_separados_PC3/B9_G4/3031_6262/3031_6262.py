def f(x):
	if x <= 1:
		return 1
	elif x >1 and x <= 2:
		return 0.5
	elif x >2 and x <= 3:
		return (x ** 2)
	else:
		return (x ** 3)
	
x = float(input())
resultado = f(x)
print(round(resultado, 2))