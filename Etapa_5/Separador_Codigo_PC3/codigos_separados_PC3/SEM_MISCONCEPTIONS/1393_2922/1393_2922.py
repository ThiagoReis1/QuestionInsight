peso = float (input ("peso: "))
tara1 = peso * 0.04 + 60
tara2 = peso * 0.05
if (peso >= 5000.0):
	print (round(tara1,2))
else:
	print (round(tara2,2))