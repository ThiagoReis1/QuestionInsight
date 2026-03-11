p = float(input("peso: "))

if (3000.0<=p<3400):
	total = p*0.8
	print(total)
	
elif(3400.0<= p <=3900.0):
	total = p*1.3
	print(total)
	
elif(3900.0 <= p <=4100.0):
	total = p*2.1
	print(total)
	
elif(p>4100.0):
	total = p*3.0
	print(total)
	