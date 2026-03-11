a = int(input())


if(a < 100):
	total = a *  0.50 + 50
	print(round(total, 2))
elif(a >= 100) and (a < 250):
	total = a * 0.75 + 50
	print(round(total, 2))
elif(a > 250) and (a < 500):
	total = a * 1.00 + 50
	print(round(total, 2))
elif(a >= 500):
	total = a * 1.25 + 50
	print(round(total, 2))
	  
	

