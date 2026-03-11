p = float(input("pesodaencomenda"))
q = 0.04*p+60
if (p <= 4999.9):
	print(round(p*0.05,2))
else:
	print(round(q,2))