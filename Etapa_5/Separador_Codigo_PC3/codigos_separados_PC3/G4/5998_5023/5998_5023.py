n = int(input("Numero de macas: "))
if (n < 12):
	t = n * 0.30
else:
	t = n * 0.25
print(round(t,2))