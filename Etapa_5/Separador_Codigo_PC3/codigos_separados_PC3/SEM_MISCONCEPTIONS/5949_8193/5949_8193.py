BC = input("bolo_ou_croassant:").upper()
fatias = int(input("fatias:"))
c = int(input("cappuccions:"))

if (BC=="B"):
	valor= fatias*3+(c*5.50)
else:
	valor= fatias*6+(c*5.50)
print(round(valor, 2))