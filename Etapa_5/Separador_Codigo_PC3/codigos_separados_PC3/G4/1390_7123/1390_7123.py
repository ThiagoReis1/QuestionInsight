c = float(input("digite o consumo:"))
			 
if c < 100 :
	t = 1.20 * c
			 
else: 
	t = 1.40 * c + 25

print(round(t, 2))