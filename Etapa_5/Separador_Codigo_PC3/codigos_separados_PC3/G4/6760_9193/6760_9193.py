r = int(input("Quanidade de roupas a serem lavadas: "))

if r > 10:
	a = 30 + 6
elif r == 10:
	a = 30 + 4.5
else:
	a = 30 + 3.25
	
print(round(a, 2))