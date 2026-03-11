qdc= float(input("Quantidade de combustivel:"))

if (0<qdc<17.5):
	print(qdc+10.5)
	
elif (17.5<=qdc<=35):
	print(qdc+14)
	
elif (35<=qdc<=50):
	print(qdc+18.6)
	
else:
	print(qdc+24.5)
	
	