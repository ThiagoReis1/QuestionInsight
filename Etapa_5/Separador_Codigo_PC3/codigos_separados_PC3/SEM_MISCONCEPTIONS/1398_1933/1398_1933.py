voo = float(input("tempo de voo:"))
inf200 = 5000 + voo * 100
sup200 = 28000 + (voo - 200) * 90
if(voo <= 200):
	print(round(inf200,2))
else:
	print(round(sup200,2))