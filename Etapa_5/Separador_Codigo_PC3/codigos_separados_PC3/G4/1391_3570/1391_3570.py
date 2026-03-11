con = int(input("consumo:"))

if (con <= 150):
	cob = (con*0.6) + 5
	print(round(cob,2))
else:
	cob = (con*0.75) + 16
	print(round(cob,2))