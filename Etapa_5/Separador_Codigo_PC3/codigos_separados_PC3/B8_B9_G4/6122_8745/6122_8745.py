comb = float(input("quantidade de combustivel comum: "))
if (comb < 17.5):
	mist = (comb + 0.8)
elif (comb >= 17.5) and (comb < 35.0):
	mist = (comb + 1.3)
elif (comb >= 35.0) and (comb < 50.0):
	mist = (comb + 2.1)
elif (comb >= 50.0):
	mist = (comb + 3.0)
print(round(mist,1))