r = float(input("pecas a serem lavadas: "))

if r > 10:
	a = 30 + 6.0
elif r < 10:
	a = 30 + 3.25
else:
	a = 4.50 + 30
print(round(a,2))
	