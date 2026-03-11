n = float(input("n: "))

if n>0:
	if n<17.5:
		print(round(n+10.5,1))
	elif 17.5<=n<35:
		print(round(n+14,1))
	elif 35<=n<50:
		print(round(n+18.6,1))
	else:
		print(round(n+24.5,1))