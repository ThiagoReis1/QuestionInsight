c = float(input("Carga horaria: "))
if (0 <= c <10) :
	print(round(((c*50) + 500), 2))
elif (10 < c <= 20 ):
	print(round(((c*60) + 600), 2))
elif (20 < c <= 30):
	print(round(((c*70) + 700), 2))
elif (30 < c):
	print(round(((c*80) + 800), 2))
	
	
	
