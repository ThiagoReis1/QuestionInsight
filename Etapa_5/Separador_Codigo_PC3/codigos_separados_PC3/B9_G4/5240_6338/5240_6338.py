n = int(input(""))
if (n < 100):
	f = 50 + (0.50 * n)
elif(n >= 100) and (n < 250):
	f = 50 + (0.75 * n)
elif(n >= 250) and (n < 500):
	f = 50 + (1.00 * n)
else:
	f = 50 + (1.25 * n)
print(round(f,2))