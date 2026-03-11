num = int(input("Numero de pizzas: "))

if num < 3:
	tt = (num * 5.0) + 3.0
	print(round(tt,2))
elif num == 3:
	tt = (num * 5) + 3.25
	print(round(tt,2))
else:
	tt = (num * 5) + 4.50
	print(round(tt,2))