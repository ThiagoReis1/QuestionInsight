m = input("L ou K:").upper()
v = float(input())

if(m=="K"):
	a = 2.20462*v
	print(round(a, 2))
else:
	a = v/2.20462
	print(round(a, 2))