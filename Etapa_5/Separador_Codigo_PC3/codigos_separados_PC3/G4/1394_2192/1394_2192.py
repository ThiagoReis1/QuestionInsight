ht = int(input())
if(ht <= 20):
	pg = round(float(ht * 50), 2)
	print(pg)
else:
	pg = round(float(20*50 + ((ht-20) * 70)), 2)
	print(pg)