amino= input("nome do aminoacido:")
o =float(15.9994) 
c =float(12.011) 
n =float(14.00674) 
h =float(1.0079)

if (amino.lower() == "leucina"):
	peso = (c*6)+(h*13)+(n)+(o*2)
	print(round(peso,2))
else:
	peso2=(c*6)+(h*15)+(n*2)+(o*2)
	print(round(peso2,2))