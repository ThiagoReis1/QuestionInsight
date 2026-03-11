t = float(input("Total da compra:"))
q = input("Tipo de pagamento:").lower()
if (q=='d'):
	w = t - t*(12/100)
	print(round(w,2))
elif (q == 'p'):
	w = t - t*(12/100)
	print(round(w,2))
elif (q=='c1'):
	w = t 
	print(round(w,2))
elif (q=='c2'):
	w = t + t*(7/100)
	print(round(w,2))