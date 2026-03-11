# faça seu código aqui!
d = int(input("dia:"))
if d < 15:
	cal = (175.00 * d) + 20
	print("total=", round(cal,2))
elif d > 15:
	cal = (175.00 * d) + 10
	print("total=", round(cal,2))
else:
	cal = (175.00 * d) + 16
	print("total=", round(cal,2))