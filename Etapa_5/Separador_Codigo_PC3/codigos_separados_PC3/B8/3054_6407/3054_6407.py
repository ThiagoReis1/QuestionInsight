worked_hours = float(input("insert value of hours worked: "))

if(worked_hours >= 0 and worked_hours <= 10):
	payment = (worked_hours * 50) + 500
	
elif(worked_hours > 10 and worked_hours <=20):
	payment = (worked_hours * 60) + 600
	
elif(worked_hours > 20 and worked_hours <=30):
	payment = (worked_hours * 70) + 700
	
elif(worked_hours > 30):
	payment = (worked_hours * 80) + 800
	
print(round(payment,2))
