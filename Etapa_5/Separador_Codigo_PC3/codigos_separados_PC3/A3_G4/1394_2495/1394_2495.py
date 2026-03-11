h = float(input("h: "))
h1 = h%10
h2 = h-h1
v1 = 50*h
v2 = 50*h2 + 70*h1
if(h<=20):
	print(round(50*h,2))
else:
	print(round(50*h2 + 70*h1,2))