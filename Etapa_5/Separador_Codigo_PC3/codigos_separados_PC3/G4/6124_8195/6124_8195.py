var1 = float(input('numero: '))
if(var1>= 3000.0 and var1< 3400.0):
	cal = var1*0.8
	print(round(cal,1))
elif(var1 >= 3400.0 and var1<  3900.0):
	cal1 = var1*1.3
	print(round(cal1,1))
elif(var1 >= 3900.0 and var1 < 4100.0):
	cal2 = var1*2.1
	print(round(cal2,1))
else:
	cal4 = var1*3.0
	print(round(cal4,1))