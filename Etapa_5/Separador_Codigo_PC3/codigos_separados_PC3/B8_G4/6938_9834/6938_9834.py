t = float(input("digite:"))
o = input ("(D), (P),  (C1) E (C2)")


if (o == "D") or (o=="P"):
	total = t - (t * 0.11)
	print(round(total, 2))
	
elif o == "C":
	par = input("(1) ou (2)")
	if par == "1":
		print(round(t, 2))
	else:
		total = t+ (t*0.06)
		print(round(total , 2))
		
	
	
	