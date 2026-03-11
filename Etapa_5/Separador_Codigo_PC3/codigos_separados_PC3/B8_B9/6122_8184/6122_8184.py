combustivel = int(input("combustivel comum em litros: "))
if (combustivel < 17.5):
	coaxium = combustivel + 0.8
elif (combustivel >= 17.5) and (combustivel < 35.0):
	coaxium = combustivel + 1.3
elif (combustivel >= 35.0) and (combustivel <= 50.0):
	coaxium = combustivel + 2.1
elif (combustivel >= 50.0):
	coaxium = combustivel + 3
print(round(coaxium,1))