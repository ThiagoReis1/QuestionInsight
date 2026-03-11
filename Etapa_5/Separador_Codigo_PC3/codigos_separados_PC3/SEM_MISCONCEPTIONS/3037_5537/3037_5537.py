x = float(input("Digite x: "))
if((x <= -1) or (x >= 1)):
	x = x**2
	print(round(x,4))
elif(x == 0):
	print("1")
else:
	print(round(x,4)