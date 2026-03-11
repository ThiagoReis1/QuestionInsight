e = float(input())
en = e * 0.05
ec = e * 0.04 + 60
if(e <= 4999.9):
	print(round(en, 2))
if(e >= 5000 ):
	print(round(ec, 2))