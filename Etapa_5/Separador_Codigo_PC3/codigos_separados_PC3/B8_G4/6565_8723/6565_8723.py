d = int(input("distancia "))
taxa = 50

if (d < 10):
	t = taxa + 5.50
	print("total=", round(t,2))
elif (d == 10):
	t = taxa + 7.75
	print("total=", round(t,2))
elif (d > 10):
	t = taxa + 10.00
	print("total=", round(t,2))