c = float(input("consumo de energia (em kWh): "))
c150 = c*0.60+5
c250 = c*0.65+8
c350 = c*0.70+12
cmaior = c*0.75+16
if (c<=150):
	print(c150)
elif (c<=250):
	print(c250)
elif (c<=350):
	print(c350)
else:
	print(cmaior)