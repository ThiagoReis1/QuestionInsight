combust = int(input("Qual a quantidade de combustivel? "))

if (combust<17.5):
	coax = combust + 1.5
	print(round(coax,2))
elif (combust>=17.5) and (combust<35.0):
	coax = combust + 2.3
	print(round(coax,2))
elif (combust>=35.0) and (combust<50):
	coax = combust + 3.3
	print(round(coax,2))
else:
	coax = combust + 4.7
	print(round(coax,2))