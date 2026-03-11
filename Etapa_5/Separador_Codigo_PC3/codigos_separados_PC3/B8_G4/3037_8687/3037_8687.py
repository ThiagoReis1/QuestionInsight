x = float(input("x: "))

if x <= -1 or x >= 1:
	fx = x ** 2
elif (x > -1 and x < 0) or (x > 0 and x < 1):
	fx = x
elif x == 0:
	fx = 1
print(round(fx, 4))