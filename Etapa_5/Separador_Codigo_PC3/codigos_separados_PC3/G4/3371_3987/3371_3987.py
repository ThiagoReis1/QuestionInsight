u = input(":")
v = float(input(":"))

km = 1.60934 * v
mi = (v)/1.60934

if(u == "K"):
	print(round(mi,2))
else:
	print(round(km,2))