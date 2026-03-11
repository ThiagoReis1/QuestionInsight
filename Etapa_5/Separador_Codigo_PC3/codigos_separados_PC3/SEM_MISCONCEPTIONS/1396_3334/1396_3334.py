total = float(input("valor:"))

xa = total * 0.1 + total
xb = total * 0.06 + total

if(total <= 300):
	print(round(xa,2))
	
else:
	print(round(xb,2))