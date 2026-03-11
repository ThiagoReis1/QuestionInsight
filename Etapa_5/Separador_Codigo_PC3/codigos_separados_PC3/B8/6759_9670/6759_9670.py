d= int(input("distancia de entrega: "))

if d < 10:
	total= 50+ 5.50
elif d == 10:
	total= 50 + 7.75
elif d > 10:
	total = 50 + 10
	
print(round(total, 2))

















