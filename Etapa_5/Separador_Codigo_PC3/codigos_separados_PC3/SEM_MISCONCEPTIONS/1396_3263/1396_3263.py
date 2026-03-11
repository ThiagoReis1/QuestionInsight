consumido = float(input("a: "))

calc1 = consumido * 0.10
calc2 = consumido * 0.06

if (consumido <= 300):
	a = (consumido + calc1)

else:
	a = (consumido + calc2)
	
print(round(a, 2))