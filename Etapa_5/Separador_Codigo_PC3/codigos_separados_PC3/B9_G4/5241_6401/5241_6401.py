c = float(input("Consumo de agua: "))

if(c < 10):
	v = (c * 2) + 20

elif(c >= 10) and (c < 20):
	v = (c * 2.5) + 20
	
elif(c >= 20) and (c < 40):
	v = (c * 2.75) + 20

else:
	v = (c * 3) + 20
	
print(round(v, 2))