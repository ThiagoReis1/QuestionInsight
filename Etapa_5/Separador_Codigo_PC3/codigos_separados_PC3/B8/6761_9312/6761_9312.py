vel = float(input(""))
calc1 = 60 + 4.50
calc2 = 60 + 5.50
calc3 = 60 + 6.50
if(vel<50):
	print(round(calc1,2))
elif(vel == 50):
	print(round(calc2,2))
elif(vel>50):
	print(round(calc3,2))