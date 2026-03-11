x = float(input())

if x <= -1 or x >= 1:
	x = x ** 2
elif -1 < x < 0 or 0 < x < 1:
	x = x 
else:
	x = 1

print(round(x,4))