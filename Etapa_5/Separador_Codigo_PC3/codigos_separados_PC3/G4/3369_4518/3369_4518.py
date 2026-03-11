tipo = input().upper()
vel = float(input())

if tipo == "M":
	conv = 3.6 * vel
	print(round(conv,2))
	
else:
	conv = vel / 3.6
	print(round(conv,2))