combo = input("Tipo de combo: ").upper()
q = float(input("Quantidade desejada: "))
ab= q * 30
c = (q *30)-((q* 30) *15 /100)
if(combo == "C"):
	print(round(c,2))
	
else:
	print(round(ab,2))