from math import*
q = int(input("Quantas mangas: "))

if (q < 6):
	x = 3.80
else: 
	x = 3.45
	
total = q*x
print(round(total, 2))
		