un = str(input("A medida esta em acres ou hectares? A/H ")).upper()
vlr = float(input("Qual o valor da medida?"))

if (un == "H"):
	mda = vlr * 2.47105
else:
	mda = vlr / 2.47105
	
print(round(mda,2))