a = float(input("consumo: "))

if(a <= 100):
	b = a * 1.20

else:
	b = (a * 1.40) + 25.00
	

print(round(b,2))