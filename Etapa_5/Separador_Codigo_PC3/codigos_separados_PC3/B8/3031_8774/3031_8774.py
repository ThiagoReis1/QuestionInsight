x= float(input())

if x <= 1:
	print("1")
elif 1 < x <= 2:
	print("2")
elif 2 < x <= 3:
	raiz2= x ** 2
	print(round(raiz2, 2))
elif x > 3:
	raiz3= x ** 3
	print(round(raiz3, 2))