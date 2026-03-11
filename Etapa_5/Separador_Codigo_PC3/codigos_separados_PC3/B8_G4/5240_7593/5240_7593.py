t= int(input("total ser pago: "))

if(t<100):
	print(round(0.50*t+50,2))
elif(100<=t<250):
	print(round(0.75*t+50,2))
elif(250<=t<500):
	print(round(1*t+50,2))
elif(t>=500):
	print(round(1.25*t+50,2))
	