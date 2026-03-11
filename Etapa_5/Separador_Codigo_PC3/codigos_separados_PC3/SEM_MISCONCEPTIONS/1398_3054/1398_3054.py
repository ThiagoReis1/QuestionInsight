tempvoo = float(input("informe o tempo: "))
#ct1 = 5000 + 100 * tempvoo
#ct2 = 8000 + (100 * tempvoo) + (90*(tempvoo-200))

if(tempvoo<=200):
	ct = (5000 + 100 * tempvoo)
else:
	ct = 8000 + 100 * 200 + ((tempvoo - 200) * 90)
print(round(ct, 2))
	


	
	