ce = int(input("valor: "))

if ce >= 0 and ce <= 150:
	ce = ce * 0.60 + 5
elif ce >= 150 and ce <= 250:
	ce = ce * 0.65 + 8
elif ce >= 250 and ce <= 350:
	ce = ce * 0.70 + 12
elif ce >= 350:
	ce = ce * 0.75 + 16
	
print(round(ce, 2))	