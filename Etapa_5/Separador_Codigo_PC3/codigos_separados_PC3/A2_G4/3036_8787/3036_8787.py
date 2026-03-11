x = float(input("digite x: "))

if x <= -1 or x >= 1: 
	x = x 
elif -1 < x < 0 or 0 < x < 1: 
	x = 1
else: x = 2

print(round(x, 2))