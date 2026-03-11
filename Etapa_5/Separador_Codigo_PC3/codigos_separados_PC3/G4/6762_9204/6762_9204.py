es = int(input("digite a idade do espectador:"))

if (es<12):
	pg = 20.0 + 1.25
	print(round(pg,2))

elif (es==12):
	pg = 20.0 + 2.25
	print(round(pg,2))

else:
	pg = 20.0 + 3.25
	print(round(pg,2))