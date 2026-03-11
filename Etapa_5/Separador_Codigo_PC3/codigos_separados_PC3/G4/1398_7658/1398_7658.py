tv= float(input(" tempo de voo "))
if tv < 200:
	print(round(5000+(tv*100),2))
else:	
	print(round(8000+(100*200)+90*(tv-200),2))