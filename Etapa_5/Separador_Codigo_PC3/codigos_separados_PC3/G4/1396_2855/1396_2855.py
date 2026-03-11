cons = float(input("valor consumido:"))

if(cons <= 300):
	print(round(cons/100 * 10 +  cons, 2))
else:
	print(round(cons/100 * 6 + cons, 2))