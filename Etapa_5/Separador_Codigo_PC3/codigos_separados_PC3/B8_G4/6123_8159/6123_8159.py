qcc=float(input("quantidade de combustivel comum: "))
if(qcc<17.5):
	print(round(qcc+0.8,1))
elif(17.5<qcc<35):
	print(round(qcc+1.3,1))
elif(35<qcc<50):
	print(round(qcc+2.1,1))
elif(qcc>50):
	print(round(qcc+3.0,1))