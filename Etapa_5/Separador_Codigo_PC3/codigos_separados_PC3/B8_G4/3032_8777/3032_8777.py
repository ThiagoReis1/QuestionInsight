from math import*
x = float(input("Digite o valor de x:"))
if x <= 0:
	f_x = 0
	a = f_x
	print(round(a, 4))
elif 0 < x and x <= 1:
		f_x = 1
		a = f_x
		print(round(a, 4))
elif 1 < x and x <= 2:
		f_x = sqrt(x)
		a = f_x
		print(round(a, 4))
elif x > 2:
		f_x = x ** (1/3)
		a = f_x
		print(round(a, 4))
