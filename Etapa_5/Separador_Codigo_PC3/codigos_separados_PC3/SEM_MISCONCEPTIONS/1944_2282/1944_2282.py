aminoacido = input("nome do aminoacido:")
if (aminoacido == "leucina"):
	pm = (12.011*6)+(1.0079*13)+(14.00674)+(15.9994*2)
else:
	pm = (12.011*6)+(1.0079*15)+(14.00674*2)+(15.9994*2)	
print(round(pm,2))