tempo=int(input("Determinar o tempo: "))
if tempo>0 and tempo<100:
	print(round(tempo*80.0+3000.0,2))
elif tempo>=100 and tempo<200:
	print(round(tempo*90.0+4000.0,2))
elif tempo>=200 and tempo<300:
	print(round(tempo*100.0+5000.0,2))
elif tempo>=300 and tempo>300:
	print(round(tempo*110.0+6000.0,2))